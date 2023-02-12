#### FastAPI With Python

Screenshot

![screenshot1](https://github.com/guynpnx/fast_api_python/blob/main/images/Screenshot%202566-02-12%20at%2017.22.28.png)

### main.py
        from fastapi import FastAPI
        import models,database
        from routers import blog,user,authentication


        models.Base.metadata.create_all(bind=database.engine)

        app = FastAPI()

        app.include_router(authentication.router)
        app.include_router(user.router)
        app.include_router(blog.router)

### router/blog.py
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
        def update_blog(id:int, request:schemas.BlogRequest ,db:Session = Depends(get_db),currant_user:schemas.UserBase =               Depends(oauth2.get_current_user)):
            return blog.update(id,request,db)

        @router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT,)
        def destroy(id:int,db:Session = Depends(get_db),currant_user:schemas.UserBase = Depends(oauth2.get_current_user)):
            return blog.delete(id,db)
