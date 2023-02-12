from fastapi import HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from hashing import Hash
import models,jwt_token
def login(request:OAuth2PasswordRequestForm,db:Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"This Email {request.username} is not register")
    
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect password")
    
    access_token = jwt_token.create_access_token(data={"sub":user.email})
    
    return {"access_token":access_token,"type":"bearer"}