from fastapi import FastAPI
from app.routes.todo import todoRouter
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(todoRouter)
register_tortoise(
    app=app,
    db_url="sqlite://db/dev.db",
    add_exception_handlers=True,
    generate_schemas=True,
    modules={"models": ["app.models.todo"]}
)


@app.get("/")
def root():
    return {"message": "Connected to server"}
