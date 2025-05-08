from fastapi import FastAPI

app = FastAPI()

users = {
    1: {"name": "John", "email": "john@gmail.com"},
    2: {"name": "Doe", "email": "doe@gmail.com"},
    3: {"name": "Jane", "email": "jane@gmail.com"},
    4: {"name": "Smith", "email": "smith@mail.com"}
}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in users:
        return users[user_id]
    else:
        return {"error": "User not found"}
    
@app.get("/users/")
def read_users():
    return users

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
