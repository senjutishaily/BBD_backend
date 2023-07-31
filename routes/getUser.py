from fastapi import APIRouter
from datatype.UserModel import UserModel_Getone
from controller.GetOneUserController import GetOneUser

getUser = APIRouter()

@getUser.get("/getuser")
async def root():
    return {
        "message": "Hello World",
        "method": "GET",
        "route": "/getUser"
    }

@getUser.post("/getuser")
async def root(data: UserModel_Getone):
    print(data)
    resultio = GetOneUser(data)
    return {
        "data": resultio,
        "method": "POST",
        "route": "/getUser"
    }