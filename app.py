#Подсказки 
#pip install fastapi, pip install uvicorn, pip install python-multipart
#uvicorn app:app --reload

import datetime
from typing import Annotated, Optional
from fastapi import FastAPI, Form
from pydantic import BaseModel

class Order(BaseModel):
    number : int
    startDate : datetime.date
    device : str
    problemType : str
    description : str
    client : str
    status : str
    master : Optional[str] = "Не назначен"

class UpdateOrderDTO(BaseModel):
    number : int
    status : Optional[str] = ""
    description : Optional[str] = ""
    master : Optional[str] = ""

repo = [
    Order(
        number = 1,
        startDate = "2024-11-11",
        device = "Телефон",
        problemType = "поломка экрана",
        description = "трещина",
        client = "Иван Иванович Иванов",
        status = "В обработке"
    )
]

app = FastAPI()

@app.get("/orders")
def get_orders():
    return repo

@app.post("/orders")
def post_orders(dto : Annotated[Order, Form()]):
    repo.append(dto)