from dotenv import load_dotenv, dotenv_values
from model.mysql import cursor
import jsonwebtoken

load_dotenv();

config   = dotenv_values(".env")

def GetOneUser(data):
    try:
        # decoding the token and getting the email
        token = jsonwebtoken.decode(data.token, config["SECRET"], algorithms=["HS256"])
        print(token)
        # Pass the parameter as a tuple with a trailing comma
        # Use parameterized query to prevent SQL injection
        resultant = cursor.execute("SELECT * FROM users WHERE email = %s", (token['email'],))
        result = cursor.fetchone()

        if result is not None:
            print(result)
            return {
                "data": result,
                "result": "success"
            }
        else:
            return {
                "error": "User not found"
            }
    except Exception as e:
        print(e)
        return {
            "error": str(e)
        }
