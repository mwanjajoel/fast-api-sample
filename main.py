from fastapi import FastAPI 

# intiate an app instance 
app = FastAPI()

# default get endpoint 
@app.get("/")
async def default_endpoint():
    return {" Hi": "World"}

# get a specific item id 
@app.get("/items/{item_id}")
async def read_the_item(item_id: int, q: str=None):
    return { "item_id": item_id, "q": q }

