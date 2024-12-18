from schema.borrow import Borrow,BorrowRecord
from crud.borrowrecord import borrow_record
from crud.user import users
from crud.book import books
from fastapi import HTTPException
from datetime import date



class BorrowCRUD:
    @staticmethod
    def borrow_book(borrow_data:Borrow):
        for user in users:
            if(user.id == borrow_data.user_id):
                if(user.is_active == True):
                    for book in books:
                        if(book.id == borrow_data.book_id):
                            if(len(borrow_record) == 0):
                                borrow_record.append(BorrowRecord(id=len(borrow_record)+1,**borrow_data.model_dump()))                                    
                                book.is_available = False
                                return "Book Successfully Borrowed"
                            else:
                                for record in borrow_record:
                                    if(book.is_available == False or (record.user_id == borrow_data.user_id and record.book_id == borrow_data.book_id)):
                                        raise HTTPException(status_code=403, detail="Book cannot be borrowed because it has been borrowed before or is not available")
                                    else:
                                        borrow_record.append(BorrowRecord(id=len(borrow_record)+1,**borrow_data.model_dump()))                                    
                                        book.is_available = False
                                        return "Book Successfully Borrowed"                            
                    raise HTTPException(status_code=404, detail="Book Not Found")
                else:
                    raise HTTPException(status_code=401, detail="User Account Inactive")
        raise HTTPException(status_code=404, detail="User Not Found")


    @staticmethod
    def return_book(book_id:int,user_id:int):   
        for book in books:
            if(book.id == book_id):
                for user in users:
                    if(user.id == user_id):
                        if(user.is_active == False):
                            raise HTTPException(status_code=403, detail="User Account Inactive")
                        for record in borrow_record:
                            if (record.user_id == user_id and record.book_id == book_id):
                                record.return_date = str(date.today())
                                book.is_available = True
                                return "Book has been successfully returned"                             
                        return "Book has not been borrowed by User before"
                raise HTTPException(status_code=404, detail="User Not Found")
        raise HTTPException(status_code=404, detail="Book Not Found")

                
borrow = BorrowCRUD()