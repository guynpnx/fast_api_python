from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(value:str):
        return pwd_context.hash(value)
    
    def verify(secret:str,hash:str):
        return pwd_context.verify(secret,hash)
