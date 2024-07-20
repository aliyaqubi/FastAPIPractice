from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import ArticleHBase
from db.models import DbArticleH



##>>>  Whatis: create articles by hotel
def create_article_h(db: Session, request: ArticleHBase):  
    new_article_h = DbArticleH(
        title = request.title,
        content = request.content,
        published = request.published,
        hotel_id = request.creator_id_h
    )
    db.add(new_article_h)            
    db.commit()                      
    db.refresh(new_article_h)        
    return new_article_h


##>>> Whatis: Read/retrieve articles of hotel (one)
def get_article_h(db: Session, id: int):
    article_h = db.query(DbArticleH).filters(DbArticleH.id == id).first()
    return article_h

