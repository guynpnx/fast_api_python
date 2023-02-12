
from datetime import timedelta,datetime
from jose import JWTError,jwt
import schemas

SECRET_KEY = "MySecret#2023"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data:dict):
    data_encode = data.copy()
    expire = datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_encode.update({"exp":expire})
    return  jwt.encode(data_encode,SECRET_KEY,algorithm=ALGORITHM)
    

def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,access_token=ALGORITHM)
        email:str = payload.get('sub')
        
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    return token_data
    