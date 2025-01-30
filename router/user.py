from fastapi import APIRouter
from schema.user import UserCreate, UserPatch
from crud.user import user

user_router = APIRouter()

@user_router.post("/create", status_code=201)
def create_users(data:UserCreate):
    return user.create(data)

@user_router.get("/", status_code=200)
def read_users():
    return user.read()

@user_router.get("/{id}", status_code=200)
def read_user_by_id(id:int):
    return user.read_by_id(id)

@user_router.patch("/update/{id}", status_code=200)
def update_user(id:int, data:UserPatch):
    return user.update(id,data)

@user_router.delete("/delete/{id}", status_code=200)
def delete_user(id:int):
    return user.delete(id)

@user_router.patch("/deactivate/{id}", status_code=200)
def not_active(id:int):
    return user.not_active(id)

@user_router.post("/borrow/{book_id}", status_code=200)
def borrow_a_book(user_id:int,book_id:int):
    return user.borrow_book(user_id,book_id)

@user_router.post("/return/{book_id}", status_code=200)
def return_a_book(book_id:int,user_id:int):
    return user.return_book(book_id,user_id)