from flask import Flask
import secrets
app = Flask(__name__)
# CREATE A CONFIGURATION FOR SECURING SESSION KEYS
app.config['SECRET_KEY'] = secrets.token_urlsafe(24)
import Ewire_fis_core.views