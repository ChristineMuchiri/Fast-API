from typing import Optional, List
from enum import IntEnum
from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1
    
class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description='Name of the todo')
    todo_description: str = Field(..., description='Description of todo')
    priority: Priority = Field(default=Priority.LOW, description='Priority of the todo')
    
class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    pass

all_todos= [
    {'todo_id':1, 'todo_name': 'sports', 'todo_description': 'go to gym'},
    {'todo_id':2, 'todo_name': 'read', 'todo_description': 'read 10 pages'},
    {'todo_id':3, 'todo_name': 'shop', 'todo_description': 'buy clothes'},
    {'todo_id':4, 'todo_name': 'meditate', 'todo_description': 'exam study'},
    {'todo_id':5, 'todo_name': 'study', 'todo_description': 'meditate 20 minutes'},   
]
@app.get('/')
async def read_root():
    return {"message": "Hello world"}

#path parameter
@app.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result': todo}

#query parameter        
@app.get('/todos')
def get_todos(first_n: Optional[int]= None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

@app.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1
    
    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }
    all_todos.append(new_todo)
    
    return new_todo
@app.put('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = update_todo['todo_name'] # type: ignore
            todo['todo_description'] = update_todo['todo_description'] # type: ignore
            return todo
    return "Error, not found"
        
@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    if todo['todo_id'] == todo_id: # type: ignore
        deleted_todo = all_todos.pop(index) # type: ignore
        return deleted_todo
    return "Error, not found"