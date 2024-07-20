from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser


##>>>  Howto: create users
def create_user(db: Session, request: UserBase):   ##>>> Howto: create new user in database 
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    ##>>> Whatis: create elements
    db.add(new_user)           ##>>> Howto: add new user to database }
    db.commit()                ##>>> Howto: send the operation to database }
    db.refresh(new_user)       ##>>> Howto: to add the data that be created by database itself }
    return new_user


##>>>  Howto: Read/retrieve users (all)
def get_all_user(db: Session):
    return db.query(DbUser).all()

##>>>  Howto: Read/retrieve users (one: in this case juss id)
def get_user(db: Session, id: int):
    ##>>> Trainer: Handel any exception
    return db.query(DbUser).filter(DbUser.id == id).first()

##>>>  Howto: Read/retrieve users (more than one: in this case id & email)
def get_more_user(db: Session, id: int, email: str):
    return db.query(DbUser).filter(DbUser.id == id).filter(DbUser.email == email).first()

##>>>  Howto: update users
def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    ##>>> Trainer: Handel any exception
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'

##>>>  Howto: delete users
def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    ##>>> Trainer: Handel any exception
    db.delete(user)
    db.commit()
    return 'ok'
