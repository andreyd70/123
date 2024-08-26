from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Главная страница
@app.get("/")
def read_root():
    return {"message": "Главная страница"}

# Страница администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

# Страница пользователя по ID
@app.get("/user/{user_id}")
def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Страница пользователя с параметрами в строке запроса
class UserInfo(BaseModel):
    username: str
    age: int

@app.get("/user")
def read_user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}