import json
import pickle
import numpy as np
from sklearn.svm.classes import SVR
from sklearn.neural_network import MLPRegressor
import os

from generate_random_games import windows_path, unix_path

windows_path_model = os.path.dirname(os.path.realpath(__file__))+'\\clp.pickle'
unix_path_model = os.path.dirname(os.path.realpath(__file__))+'/clp.pickle'

def load_model():
    # Save training samples to json file
    file = open(windows_path, 'r') if os.name == 'nt' else  open(
        unix_path, 'r')
    datas = json.load(file)
    # Create model object to train and predict new values
    # You can try to change this estimator and look what is the difference.
    clp = MLPRegressor(activation='tanh',solver='sgd')
    get_X = datas.get('X')
    get_Y = datas.get('Y')
    X = np.array(get_X)
    Y = np.array(get_Y)
    return X,Y,clp

if __name__=="__main__":
    X,Y,clp = load_model()
    clp.fit(X,Y)
    # Save our trained estimator into pickle file, to recover later.
    pickle.dump(clp,open(windows_path_model, 'wb') if os.name == 'nt' else  open(
        unix_path_model, 'wb'))