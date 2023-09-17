from fastapi import APIRouter

todoRouter = APIRouter(prefix="/todo", tags=["todo"])


@todoRouter.get("/")
def index():
    return ""


@todoRouter.get("/{key}")
def show(key: int):
    return ""


@todoRouter.post("/add")
def store():
    return ""


@todoRouter.put("/{key}")
def update(key: int):
    return ""


@todoRouter.delete("/{key}")
def destroy(key: int):
    return ""
