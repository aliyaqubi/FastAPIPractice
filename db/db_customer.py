from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import CustomerBase
from db.models import DbCustomer



##>>>  BookNest: create customers
def create_customer(db: Session, request: CustomerBase):   ##>>> Howto: create new user in database 
    new_customer = DbCustomer(
        firstname = request.firstname,
        secondname = request.secondname,
        username = request.username,
        password = Hash.bcrypt(request.password),
        email = request.email,
        phone = request.phone,   # ???
        adress = request.adress,
        nationality = request.nationality
    )
    ##>>> Whatis: create elements
    db.add(new_customer)           ##>>> Howto: add new user to database }
    db.commit()                    ##>>> Howto: send the operation to database }
    db.refresh(new_customer)       ##>>> Howto: to add the data that be created by database itself }
    return new_customer


##>>>  BookNest: Read/retrieve customers (all)
def get_all_customers(db: Session):
    return db.query(DbCustomer).all()

# ##>>>  Howto: Read/retrieve users (one: in this case juss id)
# def get_user(db: Session, id: int):
#     ##>>> Trainer: Handel any exception
#     return db.query(DbUser).filter(DbUser.id == id).first()

# ##>>>  Howto: Read/retrieve users (more than one: in this case id & email)
# def get_more_user(db: Session, id: int, email: str):
#     return db.query(DbUser).filter(DbUser.id == id).filter(DbUser.email == email).first()


##>>>  BookNest: update customers
def update_customer(db: Session, id: int, request: CustomerBase):
    customer = db.query(DbCustomer).filter(DbCustomer.id == id)
    customer.update({
        DbCustomer.firstname: request.firstname,
        DbCustomer.secondname: request.secondname,
        DbCustomer.username: request.username,
        DbCustomer.password: Hash.bcrypt(request.password),
        DbCustomer.email: request.email,
        DbCustomer.phone: request.phone,   # ???
        DbCustomer.adress: request.adress,
        DbCustomer.nationality: request.nationality
    })
    db.commit()
    return 'ok'


##>>>  BookNest: delete customers
def delete_customer(db: Session, id: int):
    customer = db.query(DbCustomer).filter(DbCustomer.id == id).first()
    db.delete(customer)
    db.commit()
    return 'ok'
