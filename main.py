from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool


@app.get("/")
def index():
    return "Hello World"

@app.post("/create")
def create(item: Item):
    return {"message":"Created", "data": item.name}
    


if __name__ == "__main__":
    app()