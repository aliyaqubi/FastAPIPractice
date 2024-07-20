from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import ArticleCBase
from db.models import DbArticleC



##>>>  Whatis: create articles by customer
def create_article_c(db: Session, request: ArticleCBase):  
    new_article_c = DbArticleC(
        title = request.title,
        content = request.content,
        published = request.published,
        customer_id = request.creator_id_c
    )
    db.add(new_article_c)            
    db.commit()                      
    db.refresh(new_article_c)        
    return new_article_c


##>>> Whatis: Read/retrieve articles of customer (one)
def get_article_c(db: Session, id: int):
    article_C = db.query(DbArticleC).filters(DbArticleC.id == id).first()
    return article_C

