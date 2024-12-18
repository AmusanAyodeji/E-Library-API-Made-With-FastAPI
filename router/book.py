from fastapi import APIRouter
from schema.book import BookCreate, BookPatch
from crud.book import book

book_router = APIRouter()


@book_router.post("/", status_code=201)
def create_books(data:BookCreate):
    return book.create(data)

@book_router.get("/", status_code=200)
def read_books():
    return book.read()

@book_router.get("/{id}", status_code=200)
def read_book_by_id(id:int):
    return book.read_by_id(id)

@book_router.patch("/book/{id}", status_code=200)
def update_book(id:int, data:BookPatch):
    return book.update(id,data)

@book_router.delete("/{id}", status_code=200)
def delete_book(id:int):
    return book.delete(id)

@book_router.patch("/{id}", status_code=200)
def not_available(id:int):
    return book.not_available(id)