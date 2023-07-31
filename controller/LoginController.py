from dotenv import load_dotenv, dotenv_values
from model.mysql import cursor
import jsonwebtoken

load_dotenv();

config   = dotenv_values(".env")

def LoginController(data):
    try:
        resultant = cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (data.email, data.password) );
        result = cursor.fetchone()
        print( result[1], data.password, data.email )
        if data.password != result[1]:
            token = "false";
            return {
                "token":token
            }
        else:
            token = jsonwebtoken.encode( { 'email': data.email, 'name': result[0] }, "long_string", algorithm="HS256")
            return {
                "token":token,
                "result":"success"
            }
    except Exception as e:
        print(e)
        return {
            "error": str(e)
        }
