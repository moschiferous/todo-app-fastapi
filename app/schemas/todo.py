from pydantic import BaseModel, Field
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from app.models.todo import Todo

GetTodo = pydantic_model_creator(Todo, name="Todo")


class PostTodo(BaseModel):
    title: str = Field(..., max_length=100)
    description: str


class PutTodo(BaseModel):
    title: Optional[str] = Field(None, max_length=100)
    description: Optional[str]
