from pydantic import BaseModel

class BorrowBase(BaseModel):
    user_id: int
    book_id: int
    borrow_date: str
    return_date: str

class BorrowRecord(BorrowBase):
    id: int

class Borrow(BorrowBase):
    pass