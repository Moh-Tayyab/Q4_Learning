from datetime import date
from pydantic import BaseModel, EmailStr , field_validator , constr

#Define UserCreate and UserRead models inheriting BaseModel.
  
#Constrain username to 3–20 characters using constr.
usernameStr=constr(min_length=3,max_length=20)

# Use EmailStr for email validation.
class User_Create(BaseModel):
    user_name:usernameStr
    email:EmailStr

class User_Read(User_Create):
    id:int


class Task(BaseModel):
    id:int
    title:str
    description:str
    status:str
    duedate:date
    user_id:int

class Create_Task(BaseModel):
    title:str
    description:str
    status:str
    duedate:date    

#Ensure due_date ≥ today via a @validator. 
    @field_validator("duedate")
    def validate_duedate(cls,v):
        if v < date.today():
            raise ValueError("Due date must be today or a future date")
        return v