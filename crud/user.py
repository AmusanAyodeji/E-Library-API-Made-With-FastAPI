from fastapi import HTTPException
from schema.user import User, UserCreate, UserPatch
from schema.borrow import Borrow,BorrowRecord
from crud.borrowrecord import borrow_record
from crud.book import books
from fastapi import HTTPException
from datetime import date

users = [
    User(id=1,name="John",email="john@gmail.com",is_active=True),
    User(id=2,name="Mary",email="mary@gmail.com",is_active=False),
    User(id=3,name="Mark",email="mark@gmail.com")
]


class UserCrud:
    @staticmethod
    def create(Userdata:UserCreate):
        newuser = User(id=len(users)+1,**Userdata.model_dump())
        users.append(newuser)
        return {"data":Userdata}

    @staticmethod
    def read():
        return {"message":"Successful","data":users}
    
    @staticmethod
    def read_by_id(input_id):
        for current_user in users:
            if (current_user.id == input_id):
                return current_user
        raise HTTPException(status_code=404, detail="User Not Found")
    
    @staticmethod
    def update(input_id, data:UserPatch):
        for current_user in users:
            if (current_user.id == input_id):
                updated_data = data.model_dump(exclude_defaults=True)  
                new_user=current_user.model_copy(update=updated_data)          
                users[users.index(current_user)] = new_user
                return {"message":"User Updated Successfully","data":new_user} 
        raise HTTPException(status_code=404, detail="User Not Found")

    @staticmethod
    def delete(input_id):
        for current_user in users:
            if (current_user.id == input_id):
                users.remove(current_user)
                return {"message":"User Removed"}
        raise HTTPException(status_code=404, detail="User Not Found")
    
    @staticmethod
    def not_active(input_id):
        for current_user in users:
            if (current_user.id == input_id):
                if(current_user.is_active == False):
                    return {"message": "User Account already Deactivated"}
                else:
                    current_user.is_active = False
                    return {"message": "User Account Deactivated"}
        raise HTTPException(status_code=404, detail="User Not Found") 
    
    @staticmethod
    def borrow_book(uid:int,bid:int):
        borrow_data = Borrow(user_id=uid,book_id=bid,borrow_date = str(date.today()),return_date = "Still Borrowed")
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


user = UserCrud()