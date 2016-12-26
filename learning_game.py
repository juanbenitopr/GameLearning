import json
import pickle
import numpy as np
from sklearn.svm.classes import SVR
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
windows_path = os.path.dirname(os.path.realpath(__file__))+'\\myfile.json'
unix_path = os.path.dirname(os.path.realpath(__file__))+'/myfile.json'

def load_model():
    # Save training samples to json file
    file = open(windows_path, 'r') if os.name == 'nt' else  open(
        unix_path, 'r')
    datas = json.load(file)
    # Create model object to train and predict new values
    # You can try to change this estimator and look what is the difference.
    clp = SVR(C=10,gamma=0.001)
    get_X = datas.get('X')
    get_Y = datas.get('Y')
    X = np.array(get_X)
    Y = np.array(get_Y)
    return X,Y,clp

if __name__=="__main__":
    X,Y,clp = load_model()
    clp.fit(X,Y)
    # Save our trained estimator into pickle file, to recover later.
    pickle.dump(clp,open('C:\\Users\\juanb\\PycharmProjects\\GameLearning\\clp.pickle', 'wb'))