from typing import List
from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user

##>>>  Whatis: create a router for users
router = APIRouter(       
    prefix= '/user',
    tags= ['user']    
)

##>>>  Howto: create users
@router.post('/', response_model= UserDisplay)
def create_user(request: UserBase, 
                db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


##>>>  Howto: read/retrieve users (all)
@router.get('/', response_model= List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_user(db)

##>>>  Howto: read/retrieve user (one)
@router.get('/{id}', response_model= UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)

##>>>  Howto: read/retrieve user (more than one)
@router.get('/{id}/email', response_model= UserDisplay)
def get_more_user(id: int, email: str, db: Session = Depends(get_db)):
    return db_user.get_more_user(db, id, email)


##>>>  Howto: update users
@router.put('/{id}')               ##>>>change to .put in class with Jurgen
#@router.post('/{id}/update')       ##>>> trainer did it with .post instesd of .put
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)


##>>>  Howto: delete users
@router.delete('/{id}')           ##>>>change to .delete in class with Jurgen
#@router.get('/{id})/delete')     ##>>> trainer did it with .get instesd of .delete
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)









