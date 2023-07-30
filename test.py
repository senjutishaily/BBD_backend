from dotenv import load_dotenv, dotenv_values
load_dotenv()
config   = dotenv_values(".env")

host     = config['HOST']
print(host)