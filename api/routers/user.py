from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from data import crud, models, schemas
from data.schemas import user_schema
from dependencies import get_db

router = APIRouter(
    prefix="/api/user",
    tags=["user"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "b762913ec414ede61808ac433c73fd0660d78ea60ef7ae45804c62f0c6c18c15"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db: Session, username: str):
    user_in_db = crud.get_user_by_username(db, username)
    return user_in_db


def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user or not user.is_active or not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = str(payload.get("sub"))
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(db, username=str(token_data.username))
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=401, detail="Inactive user")
    return current_user


def get_current_active_admin_user(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=401, detail="Inactive user")
    if not current_user.is_admin:
        raise HTTPException(
            status_code=403, detail="No permission")
    return current_user


@router.post("/login", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=user_schema.User)
def read_users_me(current_user: models.User = Depends(get_current_active_user)):
    return current_user


@router.post("/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=List[user_schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=user_schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/me/update-password", response_model=schemas.BaseRet)
def update_password(update_password: user_schema.UpdatePassword, current_user: models.User = Depends(get_current_active_user)):
    if current_user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    ret = schemas.BaseRet(result="success", message="成功")
    if update_password.new != update_password.confirm:
        ret.result = "fail"
        ret.message = "新密码和确认密码不一致"
        return ret
    if not verify_password(update_password.old, current_user.password):
        ret.result = "fail"
        ret.message = "旧密码错误"
        return ret
    return ret


#logout
@router.post("/me/logout", response_model=schemas.BaseRet)
def logout():
    ret = schemas.BaseRet(result="success", message="成功")
    return ret

@router.post("/admin/init")
def admin_init(admin: user_schema.UserCreate, db: Session = Depends(get_db)):
    count_admin = crud.count_admin(db)
    if count_admin > 0:
        raise HTTPException(
            status_code=400, detail="Admin already registered")
    return crud.create_admin(db=db, user=admin)


@router.post("/admin/users", response_model=user_schema.UserCreateRet)
def admin_add_user(user: user_schema.UserCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_admin_user)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=409, detail="Username already registered")
    return crud.create_user(db=db, user=user)
