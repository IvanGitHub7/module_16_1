from fastapi import FastAPI

#uvicorn module_16_1:app --reload

app = FastAPI()

@app.get("/")
async def welcome() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_id(user_id:int) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}")
async def user_info(username:str, age:int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."

