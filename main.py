from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    item: str
    done: bool

@app.post('/todo')
def create_todo():
    pass

@app.get('/todo')
def get_todos():
    pass

@app.get('/todo/{id}')
def get_todo():
    pass

@app.put('/todo/{id}')
def update_todo():
    pass

@app.delete('/todo/{id}')
def delete_todo():
    pass
