# app/routers/todo.py

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.todo import Todo, TodoCreate, TodoRead, TodoUpdate
from app.database.database import get_session
from typing import List

router = APIRouter()

@router.post("/", response_model=TodoRead)
def create_todo(todo: TodoCreate, session: Session = Depends(get_session)):
    db_todo = Todo.from_orm(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.get("/", response_model=List[TodoRead])
def read_todos(session: Session = Depends(get_session)):
    todos = session.exec(select(Todo)).all()
    return todos

@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.patch("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo: TodoUpdate, session: Session = Depends(get_session)):
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.delete("/{todo_id}", response_model=TodoRead)
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    session.commit()
    return todo
