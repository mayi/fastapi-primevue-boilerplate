from fastapi import FastAPI
from routers import user
from data import models
from data.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
