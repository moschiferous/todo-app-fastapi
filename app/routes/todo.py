from fastapi import APIRouter, HTTPException, status
from app.models.todo import Todo
from app.schemas.todo import GetTodo, PostTodo, PutTodo

todoRouter = APIRouter(prefix="/todo", tags=["todo"])


@todoRouter.get("/")
async def index():
    data = Todo.all()
    return await GetTodo.from_queryset(data)


@todoRouter.get("/{key}", response_model=GetTodo)
async def show(key: int):
    exist = await Todo.filter(id=key).exists()
    if not exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return await GetTodo.from_queryset_single(Todo.get(id=key))


@todoRouter.post("/add")
async def store(body: PostTodo):
    await Todo.create(**body.model_dump(exclude_unset=True))
    return {"message": "Todo added!"}


@todoRouter.put("/{key}")
async def update(key: int, body: PutTodo):
    data = body.model_dump(exclude_unset=True)
    exist = await Todo.filter(id=key).exists()
    if not exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await Todo.filter(id=key).update(**data)
    return {"message": "Todo updated!"}


@todoRouter.delete("/{key}")
async def destroy(key: int):
    exist = await Todo.filter(id=key).exists()
    if not exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await Todo.filter(id=key).delete()
    return {"message": "Todo deleted!"}
