from flask import Flask
from flask_restful import Api
import numpy as np

from predict import Predict


APP = Flask(__name__)
API = Api(APP)


API.add_resource(Predict, '/predict')


if __name__ == "__main__":
    # Please do not set debug=True in production
    APP.run(host="0.0.0.0", port=5000, debug=True)
