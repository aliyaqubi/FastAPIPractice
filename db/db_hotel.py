from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import HotelBase
from db.models import DbHotel


##>>>  BookNest: create hotels
def create_hotel(db: Session, request: HotelBase):   ##>>> Howto: create new hotel in database 
    new_hotel = DbHotel(
        name = request.name,
        #manager = request.manager,
        username = request.username,
        password = Hash.bcrypt(request.password),
        email = request.email,
        phone = request.phone, # ???
        adress = request.adress,
        country = request.country,
        city = request.city, 
        rooms = request.rooms # ???    
    )
    ##>>> Whatis: create elements
    db.add(new_hotel)           ##>>> Howto: add new hotel to database 
    db.commit()                 ##>>> Howto: send the operation to database 
    db.refresh(new_hotel)       ##>>> Howto: to add the data that be created by database itself 
    return new_hotel


##>>>  BookNest: Read/retrieve hotels (all)
def get_all_hotels(db: Session):
    return db.query(DbHotel).all()

# ##>>>  Howto: Read/retrieve hotels (one)
# def get_user(db: Session, id: int):
#     ##>>> Trainer: Handel any exception
#     return db.query(DbUser).filter(DbUser.id == id).first()

# ##>>>  Howto: Read/retrieve hotels (more than one)
# def get_more_user(db: Session, id: int, email: str):
#     return db.query(DbUser).filter(DbUser.id == id).filter(DbUser.email == email).first()


##>>>  BookNest: update hotels
def update_hotel(db: Session, id: int, request: HotelBase):
    hotel = db.query(DbHotel).filter(DbHotel.id == id)
    hotel.update({
        DbHotel.name: request.name,
        #DbHotel.manager: request.manager,
        DbHotel.username: request.username,
        DbHotel.password: Hash.bcrypt(request.password),
        DbHotel.email: request.email,
        DbHotel.phone: request.phone, # ???
        DbHotel.adress: request.adress,
        DbHotel.country: request.country,
        DbHotel.city: request.city, 
        DbHotel.rooms: request.rooms # ???  
        
    })
    db.commit()
    return 'ok'

##>>>  BookNest: delete hotels
def delete_hotel(db: Session, id: int):
    hotel = db.query(DbHotel).filter(DbHotel.id == id).first()
    db.delete(hotel)
    db.commit()
    return 'ok'
