from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    nickname: str


class UserCreate(UserBase):
    password: str


class UserCreateRet(UserBase):
    id: str


class UserUpdate(BaseModel):
    is_active: Optional[bool]


class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True


class UpdatePassword(BaseModel):
    old: str
    new: str
    confirm: str


class ResetPassword(BaseModel):
    password: str
