import pickle
import numpy as np
from sklearn import preprocessing
from sklearn.svm.classes import SVR

from learning_game import load_model


def get_awards():
    award = 20+30*np.random.random_sample(16)
    np_sum = np.sum(award)
    final_award = np.concatenate((award, np.array([np_sum])))
    return final_award

def possible_fail():
    stop = int(np.random.random_sample() * 15 + 1)
    return stop-1

if __name__ == "__main__":
    # x,y,clp = load_model()
    # clp.fit(x, y)
    clp = pickle.load(open(r'C:\\Users\\juanb\\PycharmProjects\\GameLearning\\clp.pickle', 'rb'))
    results = np.zeros(100)
    max_result = np.zeros(100)
    round_stop_log = []
    count = 0
    for i in range(100):
        awards = get_awards()
        predicted = clp.predict(awards.reshape(1,-1))
        fail = possible_fail()
        round_stop = int(round(predicted[0]))
        round_stop_log.append(round_stop)
        if round_stop <= fail:
            results[count] = np.sum(awards[0:round_stop])
        max_result[count] = np.sum(awards[0:fail])
        count+=1
    for i in range(100):
        print (str(round_stop_log[i])+" "+str(results[i])+" "+str(max_result[i]))
