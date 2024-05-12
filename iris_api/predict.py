import pickle
from flask_restful import Resource, reqparse
import numpy as np

MODEL_SRC = 'pkl'

MODELS = dict({
    "LR": {
        'desc': 'Logistic Regression',
        'model': pickle.load(open(f'{MODEL_SRC}/iris_LogisticRegression.pkl', 'rb'))
    },
    "KNN": {
        'desc': 'K-Nearest Neighbours',
        'model': pickle.load(open(f'{MODEL_SRC}/iris_KNeighborsClassifier.pkl', 'rb'))
    },
})


class Predict(Resource):

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('classifier')
        parser.add_argument('petal_length')
        parser.add_argument('petal_width')
        parser.add_argument('sepal_length')
        parser.add_argument('sepal_width')


        args = parser.parse_args()  # creates dict
        classifier = args['classifier']
        args.pop('classifier') # Pop as it is not needed by the model itself
        
        if classifier not in MODELS.keys():
            known_models = dict({})
            
            for key in MODELS.keys():
                known_models[key] = MODELS[key]["desc"]
            
            out = {
                'Error' : f'Unknown model {classifier}',
                'Known Models': known_models
            }
            
            return out, 500

        # convert input to array
        X_new = np.fromiter(args.values(), dtype=float)

        out = {'Prediction': MODELS[classifier]['model'].predict([X_new])[0]}

        return out, 200
