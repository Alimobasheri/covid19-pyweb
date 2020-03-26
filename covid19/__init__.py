from flask import Flask
app = Flask(__name__)

from covid19 import routes
