from fastapi import FastAPI ,HTTPException
from schemas import User_Create , Task ,User_Read , Create_Task
from memory import USERS ,TASKS

#FastAPI Endpoints
app=FastAPI(
    title="Task Tracker API",
    description="this app will handle task tracking"
)
user_id=1
task_id=1

@app.get("/")
def main_route():
    return {"messge":"Task Tracking app is running"}

#UsersPOST /users/ – create a user (return UserRead).

@app.post("/user/",response_model=User_Read)
def create_user(user:User_Create):
    global user_id
    new_user=User_Read(id=user_id, **user.model_dump())
    USERS[user_id]=new_user
    user_id += 1
    return new_user

#GET /users/{user_id} – retrieve user.
@app.get("/get-user/{user_id}")
def get_all_user(user_id:int):
    user=USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404,detail=f"user id {user_id} not found")
    return user

#Tasks
#POST /tasks/ – create a task (return full Task model).

@app.post("/user/{user_id}/task",response_model=Task)
def create_task(task:Create_Task,user_id:int):
    global task_id
    new_task=Task(user_id=user_id,id=task_id, **task.model_dump())
    TASKS[task_id]=new_task
    task_id += 1
    return new_task

# GET /tasks/{task_id} – get task.

@app.get("/tasks/{task_id}")
def get_all_task(task_id:int):
    task=TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404,detail=f"Task {task_id} not found")
    return  task



# PUT /tasks/{task_id} – update status only, validating allowed values. 
@app.put("/tasks/{task_id}")
def status_update(task_id:int,status:str):
    if status.lower() not in {"pending","done","in progress"}:
        raise HTTPException(status_code=400,detail=f"{status} is not a valid status ")
    task=TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404,detail=f"no task found")
    task.status=status
    return task

    
# GET /users/{user_id}/tasks – list all tasks for a user.

@app.get("/users/{user_id}/tasks")
def users_tasks(user_id:int):
    lst=[]
    for task in TASKS.values():
        if task.user_id == user_id:
            lst.append(task)
    return {"data":lst }