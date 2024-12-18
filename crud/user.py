from fastapi import HTTPException
from schema.user import User, UserCreate, UserPatch

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

user = UserCrud()