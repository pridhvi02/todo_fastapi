# app/main.py

from fastapi import FastAPI
from app.database.database import create_db_and_tables
from app.routers import todo

app = FastAPI()

# Include router
app.include_router(todo.router, prefix="/todos", tags=["todos"])

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# For serving templates
@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo App"}
