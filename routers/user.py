from fastapi import APIRouter ,status,Depends
from sqlalchemy.orm import Session
import schemas 
from database import get_db
from repositories import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/",response_model=schemas.UserResponse,status_code=status.HTTP_201_CREATED)
def create(request : schemas.UserRequest ,db:Session = Depends(get_db)):
    return user.create(request,db)

@router.get("/{id}",response_model=schemas.UserResponse)
def get_user_by_id(id:int,db:Session = Depends(get_db)):
    return user.get_user_by_id(id,db)