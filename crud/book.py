from fastapi import HTTPException
from schema.book import Book, BookCreate, BookPatch

books = [
    Book(id=1,title="Book1",author="Author1",is_available=True),
    Book(id=2,title="Book2",author="Author2",is_available=True),
    Book(id=3,title="Book3",author="Author3",is_available=True)
]

class BookCrud:
    @staticmethod
    def create(Bookdata:BookCreate):
        newbook = Book(id=len(books)+1,**Bookdata.model_dump())
        books.append(newbook)
        return {"data":Bookdata}

    @staticmethod
    def read():
        return {"message":"Successful","data":books}
    
    @staticmethod
    def read_by_id(input_id):
        for current_book in books:
            if (current_book.id == input_id):
                return current_book
        raise HTTPException(status_code=404, detail="Book Not Found")
    
    @staticmethod
    def update(input_id, data:BookPatch):
        for current_book in books:
            if (current_book.id == input_id):
                updated_data = data.model_dump(exclude_defaults=True)  
                new_book=current_book.model_copy(update=updated_data)          
                books[books.index(current_book)] = new_book
                return {"message":"Book Updated Successfully","data":new_book} 
        raise HTTPException(status_code=404, detail="Book Not Found")

    @staticmethod
    def delete(input_id):
        for current_book in books:
            if (current_book.id == input_id):
                books.remove(current_book)
                return {"message":"Book Removed"}
        raise HTTPException(status_code=404, detail="Book Not Found")
    
    @staticmethod
    def not_available(input_id):
        for current_book in books:
            if (current_book.id == input_id):
                if(current_book.is_available == False):
                    return {"message": "Book Already Unavailable"}
                else:
                    current_book.is_available = False
                    return {"message": "Book has been made unavailable"}
        raise HTTPException(status_code=404, detail="Book Not Found") 

book = BookCrud()