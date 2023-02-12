from fastapi import APIRouter ,status,Depends,HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from repositories import blog
import schemas,models,oauth2


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
    
)

@router.post("/",status_code=status.HTTP_201_CREATED,)
def create_blog(request:schemas.BlogRequest, db:Session = Depends(get_db),currant_user:schemas.UserBase = Depends(oauth2.get_current_user)):
    return blog.create(request,db,currant_user)


@router.get("/",response_model=List[schemas.BlogResponse])
def get_blogs(db:Session = Depends(get_db),currant_user:schemas.UserBase = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.get("/{id}",response_model=schemas.BlogResponse,)
def get_blog_by_part(id:int,db:Session = Depends(get_db),currant_user:schemas.UserBase = Depends(oauth2.get_current_user)):
    return blog.get_blog_by_id(id,db)

@router.patch("/{id}",status_code=status.HTTP_202_ACCEPTED,)
def update_blog(id:int, request:schemas.BlogRequest ,db:Session = Depends(get_db),currant_user:schemas.UserBase = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT,)
def destroy(id:int,db:Session = Depends(get_db),currant_user:schemas.UserBase = Depends(oauth2.get_current_user)):
    return blog.delete(id,db)