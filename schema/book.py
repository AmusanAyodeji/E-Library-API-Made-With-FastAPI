from pydantic import BaseModel

class BookBase(BaseModel):
    title: str = "Book1"
    author: str = "Author1"
    is_available: bool = True

class Book(BookBase):
    id: int

class BookCreate(BookBase):
    pass

class BookPatch(BookBase):
    title: str = "DefaultBook"
    author: str = "DefaultAuthor"
    is_available: bool = None