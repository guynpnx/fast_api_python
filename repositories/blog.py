from fastapi import HTTPException,status
from sqlalchemy.orm import Session
import models,schemas

def create(request:schemas.BlogRequest,db:Session,currant_user):
    user_email = currant_user.email
    user = db.query(models.User).filter(models.User.email == user_email).first()
    new_blog = models.Blog(title = request.title,body= request.body,user_id=user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog

def get_all(db:Session):
    return db.query(models.Blog).all()

def get_blog_by_id(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog id {id} have no")
        
    return blog.first()

def update(id:int,request:schemas.BlogRequest,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog id {id} have no")
    
    blog.update(request.dict())
    db.commit()
    
    return blog.first()

def delete(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Blog id {id} have no")

    blog.delete(synchronize_session=False)
    db.commit()
    
    return "done"