from sqlalchemy.orm import Session


from data import models
from data.schemas import (
    user_schema,
)
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_password_hash(password):
    return pwd_context.hash(password)


def create_user(db: Session, user: user_schema.UserCreate):
    db_user = models.User(
        username=user.username,
        nickname=user.nickname,
        hashed_password=get_password_hash(user.password),
        is_admin=False,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        "username": db_user.username,
        "nickname": db_user.nickname,
        "id": db_user.id,
        "is_admin": db_user.is_admin,
        "is_active": db_user.is_active,
    }


def create_admin(db: Session, user: user_schema.UserCreate):
    db_user = models.User(
        username=user.username,
        nickname=user.nickname,
        hashed_password=get_password_hash(user.password),
        is_admin=True,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        "username": db_user.username,
        "nickname": db_user.nickname,
        "id": db_user.id,
    }


def count_admin(db: Session):
    return db.query(models.User).filter(models.User.is_admin == True).count()


def update_user(db: Session, id: int, update_user: user_schema.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if db_user:
        update_dict = update_user.dict(exclude_unset=True)
        for k, v in update_dict.items():
            setattr(db_user, k, v)
        db.commit()
        db.flush()
        db.refresh(db_user)
        return db_user
    return None
