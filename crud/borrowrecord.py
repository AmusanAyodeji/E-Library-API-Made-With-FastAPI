from fastapi import HTTPException

borrow_record = []

class Records:
    @staticmethod
    def records():
        return {"message":"Successful","data":borrow_record}
    
    @staticmethod
    def record_by_id(user_id:int):
        user_record = []
        for record in borrow_record:
            if(record.user_id == user_id):
                user_record.append(record)
        if(len(user_record) == 0):
            raise HTTPException(status_code=404, detail="User Record Not Found")
        else:
            return {"message":"User record Found","data":user_record}
        
record = Records()
