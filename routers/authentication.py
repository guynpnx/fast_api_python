from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from repositories import authentication
import schemas
router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    return authentication.login(request,db)

