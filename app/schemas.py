from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional, Annotated

from pydantic.types import conint

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)



class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass

#handles the responses
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    #do we need the following? what it is for? (maybe it was needed for older versions?)
    model_config = ConfigDict(from_attributes=True)

class PostOut(BaseModel):
    Post:Post 
    votes: int 
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None # not the same as in th tutoiral -> Optional[str]


class Vote(BaseModel):
    post_id:int 
    dir: Annotated[int, Field(le=1)]
