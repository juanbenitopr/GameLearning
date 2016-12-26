import json
import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
windows_path = os.path.dirname(os.path.realpath(__file__))+'\\myfile.json'
unix_path = os.path.dirname(os.path.realpath(__file__))+'/myfile.json'

def get_awards():
    # This Game always have 16 round
    award = 20+30*np.random.random_sample(16)
    np_sum = np.sum(award)
    final_award = np.concatenate((award, np.array([np_sum])))
    # Final_award is the variable which contains an array with the money for each round
    return final_award

def get_best_choice():
    # Never the round stop will be zero, and the max will be 16
    stop = int(np.random.random_sample() * 15 + 1)
    return stop

if __name__ == "__main__":
    award = np.zeros((1000,17),)
    Y = np.zeros(1000)
    count = 0
    for i in range(1000):
        award[count,:] = get_awards()
        Y[count]=get_best_choice()
        count+=1
    datas = {'X':award.tolist(),'Y':Y.tolist()}


    file = open(windows_path, 'w') if os.name == 'nt' else  open(
        unix_path, 'w')
    load = json.dumps(datas)
    file.write(load)
    file.close()