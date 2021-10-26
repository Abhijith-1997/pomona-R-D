from os import environ
from Ewire_fis_be import app
if __name__ == '__main__':
    HOST = '192.168.0.225'
    # # HOST = environ.get("SERVER_HOST","127.0.0.1")
    # HOST = environ.get("SERVER_HOST","192.168.0.225")
    try :
        PORT = int(environ.get('SERVER_PORT','8003'))
    except ValueError:
        PORT = 8000

app.run(HOST,PORT,debug=True)