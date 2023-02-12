from fastapi import FastAPI
import models,database
from routers import blog,user,authentication


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)