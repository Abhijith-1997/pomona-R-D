from os import environ
from Fis_Ewire_Api.views import app

if __name__ == "__main__":
    HOST = environ.get("SERVER_HOST","127.0.0.1")
    try:
        PORT = int(environ.get("SERVER_PORT","8005"))
    except ValueError:
        PORT =8001

app.run(HOST,PORT,debug= True)