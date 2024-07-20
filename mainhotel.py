from fastapi import FastAPI
from router import customer
from router import hotel
from db import models
from db.database import engine


app = FastAPI()
app.include_router(customer.router)
app.include_router(hotel.router)


models.Base.metadata.create_all(engine) 