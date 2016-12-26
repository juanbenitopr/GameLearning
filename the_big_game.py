import pickle
import numpy as np
from tkinter import *
from tkinter import ttk

from learning_game import load_model

class GameRound():
    def __init__(self):
        self.round = 0
        self.awards = get_awards()
        self.stop_round = get_stop_round()
        self.results =0

    def get_award_round(self):
        return self.awards[self.round]

    def get_round(self):
        return self.round

    def next_round(self):
        if self.round<self.stop_round:
            self.results += self.get_award_round()
            self.round += 1
            round_label.set(str(game.round)+"/16")
            results_label.set(self.results)
            awards_label.set(self.get_award_round())
        else:
            round_label.set(0)
            results_label.set("Lose!")
            awards_label.set(0)
            results_machine_label.set(np.sum(self.awards[0:self.get_machine_round()])) if self.get_machine_round()<self.stop_round else results_machine_label.set("Machine Lost")

    def get_machine_round(self):
        clp = pickle.load(open(r'C:\\Users\\juanb\\PycharmProjects\\GameLearning\\clp.pickle', 'rb'))
        predicted = clp.predict(self.awards.reshape(1,-1))
        round_stop_machine = int(round(predicted[0]))
        return round_stop_machine

    def stop_game(self):
        if self.get_machine_round()<self.stop_round:
            results_machine_label.set(np.sum(self.awards[0:self.get_machine_round()]))
        else:
            results_machine_label.set("Machine Lose")


def get_awards():
    award = 20+30*np.random.random_sample(16)
    np_sum = np.sum(award)
    final_award = np.concatenate((award, np.array([np_sum])))
    return final_award

def get_stop_round():
    stop = int(np.random.random_sample() * 15 + 1)
    return stop-1

def play_one_hundred_times():
    results = np.zeros(100)
    max_result = np.zeros(100)
    round_stop_log = []
    count = 0
    for i in range(100):
        awards = get_awards()
        predicted = clp.predict(awards.reshape(1,-1))
        fail = get_stop_round()
        round_stop = int(round(predicted[0]))
        round_stop_log.append(round_stop)
        if round_stop <= fail:
            results[count] = np.sum(awards[0:round_stop])
        max_result[count] = np.sum(awards[0:fail])
        count+=1
    for i in range(100):
        print (str(round_stop_log[i])+" "+str(results[i])+" "+str(max_result[i]))


def next_round(round_n):
    round_n += 1
    round.set(round_n)


if __name__ == "__main__":
    # x,y,clp = load_model()
    # clp.fit(x, y)
    game = GameRound()

    root = Tk()
    root.title("Feet to Meters")

    round_label = StringVar()
    awards_label = StringVar()
    results_label = StringVar()
    results_machine_label = StringVar()
    results_label.set(game.results)
    awards_label.set(game.get_award_round())
    round_label.set(str(game.round)+"/16")

    Button(command=game.next_round,text="Next Round").grid(row=1)
    Button(command=game.stop_game,text="Stop Game").grid(row=1,column=1)

    Label(root, text = "Round").grid(row=0,column=0)
    Label(root, textvariable = round_label).grid(row=0,column=1)

    Label(root, textvariable = awards_label).grid(row=2,column=1)
    Label(root, text = "Award this round").grid(row=2,column=0)
    Label(root, textvariable = results_label).grid(row=3,column=1)
    Label(root, text = "Results").grid(row=3,column=0)
    Label(root, text="Machine Win this:").grid(row=4,column=0)
    Label(root,textvariable=results_machine_label).grid(row=4,column=1)
    root.mainloop()

