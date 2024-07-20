from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DbArticle



##>>>  Whatis: create articles
def create_article(db: Session, request: ArticleBase):   ##>>> Howto: create new article in database 
    new_article = DbArticle(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.creator_id
    )
    ##>>> Whatis: create elements
    db.add(new_article)            ##>>> Howto: add new article to database }
    db.commit()                    ##>>> Howto: send the operation to database }
    db.refresh(new_article)        ##>>> Howto: to add the data that be created by database itself }
    return new_article


##>>> Whatis: Read/retrieve customers (one)
def get_article(db: Session, id: int):
    article = db.query(DbArticle).filters(DbArticle.id == id).first()
    return article
    ##>>> or in this way: return db.query(DbArticle).filter(DbArticle.id == id).first()
