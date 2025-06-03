from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义请求体模型
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# 根路径
@app.get("/")
def read_root():
    return {"message": "FastAPI + uv 部署示例"}

# 路径参数示例
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# POST 请求示例
@app.post("/items/")
def create_item(item: Item):
    return item