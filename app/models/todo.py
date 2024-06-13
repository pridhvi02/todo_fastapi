# app/models/todo.py

from sqlmodel import SQLModel, Field
from typing import Optional

class TodoBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: int

    class Config:
        orm_mode = True

class TodoUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
