
from fastapi import FastAPI
from router import customer
from router import hotel
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import article_c
from router import article_h
from db import models
from db.database import engine


app = FastAPI()
app.include_router(customer.router)
app.include_router(article_c.router)
app.include_router(hotel.router)
app.include_router(article_h.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message': 'Hello world!'}

models.Base.metadata.create_all(engine) 
##>>Note :if something change in structure of tables, delete <fastapi-practice.db> 
##        and run the server again.



