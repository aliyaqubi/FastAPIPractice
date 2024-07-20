from typing import List
from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article

##>>> Whatis: create a router for articles
router = APIRouter(       
    prefix= '/article',
    tags= ['article']    
)



##>>> Whatis: router for creation article
@router.post('/', response_model= ArticleDisplay)
def create_article(request: ArticleBase, 
                db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


##>>> Whatis: router for reading/retrieving articles (one)
@router.get('/{id}', response_model= ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)
