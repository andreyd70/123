from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the API!"}

@app.get("/user/{user_id}")
async def get_user(
    user_id: int = Path(..., ge=1, le=100, description="Enter User ID")
):
    return {"user_id": user_id}

@app.get("/user/{username}/{age}")
async def get_user_details(
    username: str = Path(..., min_length=5, max_length=20, description="Enter username"),
    age: int = Path(..., ge=18, le=120, description="Enter age")
):
    return {"username": username, "age": age}