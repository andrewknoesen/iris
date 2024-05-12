import os
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pickle
import numpy as np


def train(X, y, classifier_type):

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)
    classifier = classifier_type

    # fit the model
    classifier.fit(X_train, y_train)
    test_prediction = classifier.predict(X_test)
    acc = accuracy_score(y_test, test_prediction)
    print(f'Successfully trained {classifier.__class__.__name__} model with an accuracy of {acc:.2f}')

    return classifier


if __name__ == '__main__':

    iris_data = datasets.load_iris()
    X = iris_data['data']
    y = iris_data['target']

    labels = {
        0: 'iris-setosa',
        1: 'iris-versicolor',
        2: 'iris-virginica'
    }

    # rename integer labels to actual flower names
    y = np.vectorize(labels.__getitem__)(y)
    
    classifiers = [LogisticRegression(), KNeighborsClassifier()]

    # Ensure the 'pkl' directory exists
    os.makedirs('pkl', exist_ok=True)
    
    for classifier in classifiers:
        mdl = train(X, y, classifier)

        # serialize model
        pickle.dump(mdl, open(f"pkl/iris_{classifier.__class__.__name__}.pkl", "wb"))