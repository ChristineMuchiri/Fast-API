from typing import Optional
from fastapi import FastAPI

app = FastAPI()

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


@api.post('/todos')