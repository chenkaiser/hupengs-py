from typing import Union
from fastapi import FastAPI
from routers import UserRoute

app = FastAPI()
app.include_router(UserRoute.router)

@app.get("/")
async def read_root():
    return {"Hello": "Python"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


