from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str
    age: int | None = None #optional field
    email: str
    
 
user_data = {"id":1, "name":"Muhammad", "age": 20, "email":"muhammad12@gmail.com"}   
user = User(**user_data) #unpacking the dictionary
#print(user) #printing the object
# print(user.id) #accessing the attributes
print(user.model_dump()) #dumping the object to dictionary

try:
    invalid_user = User(id="not_an_int", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e)