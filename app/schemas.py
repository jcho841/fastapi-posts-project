from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


# create model: pydantic has field type that can be allowed
# can make a base model and inherit it to other classes


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

# email validator installed with fastapi


class UserCreate(BaseModel):
    email: EmailStr
    password: str


# need to hash password by installing passlib and bcrypt


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# create schema for access token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
