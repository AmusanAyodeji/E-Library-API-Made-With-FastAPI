from fastapi import APIRouter
from schema.user import UserCreate, UserPatch
from crud.user import user

user_router = APIRouter()


@user_router.post("/", status_code=201)
def create_users(data:UserCreate):
    return user.create(data)

@user_router.get("/", status_code=200)
def read_users():
    return user.read()

@user_router.get("/{id}", status_code=200)
def read_user_by_id(id:int):
    return user.read_by_id(id)

@user_router.patch("/user/{id}", status_code=200)
def update_user(id:int, data:UserPatch):
    return user.update(id,data)

@user_router.delete("/{id}", status_code=200)
def delete_user(id:int):
    return user.delete(id)

@user_router.patch("/{id}", status_code=200)
def not_active(id:int):
    return user.not_active(id)