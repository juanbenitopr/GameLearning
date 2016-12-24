import json
import pickle
import numpy as np
import sklearn
from sklearn import preprocessing
from sklearn.grid_search import GridSearchCV
from sklearn.svm.classes import SVR, NuSVR


def load_model():
    file = open(r'C:\\Users\\juanb\\PycharmProjects\\GameLearning\\myfile.json', 'r')
    datas = json.load(file)
    param_grid = [
        {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
        {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001,0.01], 'kernel': ['rbf']},
    ]
    clp = SVR(C=100,gamma=0.001)
    get_X = datas.get('X')
    get_Y = datas.get('Y')
    X = np.array(get_X)
    Y = np.array(get_Y)
    return X,Y,clp

if __name__=="__main__":
    X,Y,clp = load_model()
    clp.fit(X,Y)
    tz = clp.predict(X)
    pickle.dump(clp,open('C:\\Users\\juanb\\PycharmProjects\\GameLearning\\clp.pickle', 'wb'))