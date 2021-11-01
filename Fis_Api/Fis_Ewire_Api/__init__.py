from flask import Flask
from flask import Flask
# from Fis_Ewire_Api.config import actionEndPoints

app = Flask(__name__)

#app.secret_key = actionEndPoints.CLIENT_SECRET

import Fis_Ewire_Api.views