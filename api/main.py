from fastapi import FastAPI
from routers import user, task
from data import models
from data.database import engine
from aps import scheduler

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)

scheduler.start()

@app.get("/")
def read_root():
    return {"Hello": "World"}

