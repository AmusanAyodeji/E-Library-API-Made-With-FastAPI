from fastapi import APIRouter
from crud.borrowrecord import record

record_router = APIRouter()


@record_router.get("/",status_code=200)
def read_records(): 
    return record.records()

@record_router.get("/{id}",status_code=200)
def read_record_by_id(user_id:int):
    return record.record_by_id(user_id)