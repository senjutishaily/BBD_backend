### This app was initialized using [FASTAPI](https://fastapi.tiangolo.com/)

- install the dependecies:
` pip install -r requirements.txt `
` pip install MySQL-python `

- start the app:
` uvicorn main:app --reload --port 3200 `

# Directories:

- config: has frontend to backend connection systems
- controller: has validation functions and data insertion functions to database
- datatype: has the data type files for catching the data setn by frontend for extreme type safety
- functions: has the functions to encrypt of decrypt any given data type [string, int, float, etc.]
- model: database connection are here
- routes: handling the endpoint of a server, eg -> login endpoint, signup endpoint.