from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    item: str
    done: bool

@app.post('/todo')
def create_todo(todo: dict):
    todo['id'] = len(todos) + 1
    todo['done'] = False
    todos.append(todo)
    return todo

@app.get('/todo')
def get_todos():
    return todos

@app.get('/todo/{id}')
def get_todo(id: int, response: Response):
    for todo in todos:
        if todo['id'] == id:
            return todo
    else:
        response.status_code = 404
        return 'Item not found'

@app.put('/todo/{id}')
def update_todo():
    pass

@app.delete('/todo/{id}')
def delete_todo():
    pass
