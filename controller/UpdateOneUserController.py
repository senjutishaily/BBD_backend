from model.mysql import cursor

def Signup(data):
    try:    
        dataset: dict = {
        'email': data.email,
        'password': data.password,
        'name': data.name,
        'blood_type': data.blood_type,
        'location': data.location,
        'phoneNumber': data.phoneNumber,
        'last_donation': ''
    }

        resultant = cursor.execute("""
            UPDATE users
            SET password = %s, name = %s, blood_type = %s, location = %s, last_donation = %s, phoneNumber = %s
            WHERE email = %s
        """, (dataset['password'], dataset['name'], dataset['blood_type'], dataset['location'], dataset['last_donation'], dataset['phoneNumber'], dataset['email']))

        print(dataset, resultant)

        result = 'false result' 

        return {
            'message': "Account Created",
            "status": "true",
            "result": "success"
        }

    
    except Exception as e:
        print(e)
        return {
            'message': e,
            "status" : "success",
            "result" : 'fail'
        }