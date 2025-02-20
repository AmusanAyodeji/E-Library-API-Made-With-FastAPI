from fastapi import FastAPI
from router.book import book_router
from router.borrowrecord import record_router
from router.user import user_router

app = FastAPI()

app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(record_router, prefix="/records", tags=["Borrow Record Management"])

@app.get("/")
def home():
    return {"Message":"Welcome to the E-Library API"}