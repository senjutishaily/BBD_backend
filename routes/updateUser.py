from fastapi import APIRouter
from datatype.UserModel import UserModel_Updateone

updateUser = APIRouter()

@updateUser.get("/updateuser")
async def root():
    return {
        "message": "Hello World",
        "method": "GET",
        "route": "/index"
    }

@updateUser.post("/updateuser")
async def root(data: UserModel_Updateone):
    print(data)
    return {
        "data": data,
        "method": "POST",
        "route": "/index"
    }