from os import environ
from Ewire_fis_core import app

if __name__ == '__main__':
    # HOST = '127.0.0.1'
    HOST = environ.get("SERVER_HOST","127.0.0.1")
    try :
        PORT = int(environ.get('SERVER_PORT','8002'))
    except ValueError:
        PORT = 8000

app.run(HOST,PORT,debug=True)