from fastapi import APIRouter
from crud.borrow import borrow
from schema.borrow import Borrow

borrow_router = APIRouter()

@borrow_router.post("/borrow", status_code=200)
def borrow_a_book(data:Borrow):
    return borrow.borrow_book(data)

@borrow_router.post("/return", status_code=200)
def return_a_book(book_id:int,user_id:int):
    return borrow.return_book(book_id,user_id)