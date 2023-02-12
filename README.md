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
