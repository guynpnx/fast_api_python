from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from hashing import Hash
import models,schemas


def create(request:schemas.UserRequest,db:Session):
    hashedPassword = Hash.bcrypt(request.password)
    newUser = models.User(email = request.email,password = hashedPassword)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    
    return newUser

def get_user_by_id(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"User id {id} have no")
        
    return user.first()