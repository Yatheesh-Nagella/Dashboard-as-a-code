from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route with a path operation decorator
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Define another route with a path operation decorator and parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
