from fastapi import FastAPI, HTTPException

from model import todo_schema

app = FastAPI()

todo_list = {}

@app.get("/health")
async def read_root():
    return {"health_state": "Up and running!"}


@app.post("/todos")
async def create_todo(todo: todo_schema):
    if todo.completed not in [True, False]:
        raise HTTPException(status_code=400, detail="Invalid value for completed field")
    if todo.id <= 0:
        raise HTTPException(status_code=400, detail="ID must be a positive integer")
    if todo.id in todo_list.keys():
        raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    
    todo_list[todo.id] = todo
    return {"message": "Todo created successfully", "todo": todo}


@app.get("/todos")
async def get_todos():
    return {"message": "List of todos", "todos": todo_list}


@app.get("/todos/{id}")
async def get_todo(id: int):
    if id <= 0:
        raise HTTPException(status_code=400, detail="ID must be a positive integer")
    if id not in todo_list.keys():
        raise HTTPException(status_code=400, detail="Todo with this ID not found")
    
    return {"message": "Todo retrieved successfully", "todo": todo_list[id]}


@app.put("/todos/{id}")
async def update_todo(id: int, todo: todo_schema):
    if id <= 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.completed not in [True, False]:
        raise HTTPException(status_code=400, detail="Invalid value for completed field")
    if id not in todo_list.keys():
        raise HTTPException(status_code=400, detail="Todo with this ID not found")
    
    
    todo_list[id] = todo
    return {"message": "Todo updated successfully", "todo": todo}


@app.delete("/todos/{id}")
async def delete_todo(id: int):
    if id <= 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    if id not in todo_list.keys():
        raise HTTPException(status_code=404, detail="Todo with this ID not found")
    
    del todo_list[id]
    return {"message": "Todo deleted successfully", "id": id}

