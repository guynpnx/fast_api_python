from pydantic import BaseModel
from typing import List,Optional

class BlogBase(BaseModel):
    title:str
    body:str
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email : str
    password : str
    
class ShowUser(BaseModel):
    email : str
    class Config:
        orm_mode = True
    
class UserRequest(UserBase):
    class Config:
        orm_mode = True
        
class UserResponse(BaseModel):
    email: str
    blogs : List[BlogBase] = []
    class Config:
        orm_mode = True


class BlogRequest(BlogBase):
    class Config:
        orm_mode = True
        
class BlogResponse(BlogBase):
    title:str
    body:str
    creator : ShowUser
    class Config:
        orm_mode = True
        

class LoginRequset(BaseModel):
    email:str
    password:str
    
class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
    email:Optional[str]= None