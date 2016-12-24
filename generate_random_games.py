import json
import numpy as np

def get_awards():
    award = 20+30*np.random.random_sample(16)
    np_sum = np.sum(award)
    final_award = np.concatenate((award, np.array([np_sum])))
    return final_award

def get_best_choice():
    stop = int(np.random.random_sample() * 15 + 1)
    return stop-1

if __name__ == "__main__":
    award = np.zeros((1000,17))
    Y = np.zeros(1000)
    count = 0
    for i in range(1000):
        award[count,:] = get_awards()
        Y[count]=get_best_choice()
        count+=1
    datas = {'X':award.tolist(),'Y':Y.tolist()}
    file = open(r'C:\\Users\\juanb\\PycharmProjects\\GameLearning\\myfile.json', 'w')
    load = json.dumps(datas)
    file.write(load)
    file.close()