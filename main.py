from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    item: str
    done: bool

@app.post('/todo')
def create_todo(new_todo: Todo):
    todo = new_todo.dict()
    todo['id'] = len(todos) + 1
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
def update_todo(id: int, updated_todo: Todo, response: Response):
    updated_todo = updated_todo.dict()
    for todo in todos:
        if todo['id'] == id:
            todo['item'] = updated_todo.get('item')
            todo['done'] = updated_todo.get('done')
            return updated_todo
    else:
        response.status_code = 404
        return 'Item not found'

@app.delete('/todo/{id}')
def delete_todo(id: int):
    for todo in todos:
        if todo['id'] == id:
            todos.remove(todo)
            return 'Item deleted successfully'
    else:
        return 'Item not found'
