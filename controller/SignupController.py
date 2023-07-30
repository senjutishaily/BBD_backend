from model.mysql import cursor


def Signup(data):
    try:    
        dataset: dict = {
            'email': data.email,
            'password': data.password,
            'name': data.name,
            'blood_type': data.blood_type,
            'location': data.location,
            'last_donation': ''
        }
        # apply validation here
        resultant = cursor.execute("INSERT INTO users (email, password, name, blood_type, location, last_donation) VALUES (%s, %s, %s, %s, %s, %s)", (dataset['email'], dataset['password'], dataset['name'], dataset['blood_type'], dataset['location'], dataset['last_donation']));
        print( dataset, resultant )
        result = 'false result'
        return {
            'message': "Account Created",
            "status" : "success",
            "result" : result
        }
    
    except Exception as e:
        print(e)
        return {
            'message': e,
            "status" : "success",
            "result" : 'fail'
        }