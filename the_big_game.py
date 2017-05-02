import pickle
import numpy as np
from tkinter import *
import os

from learning_game import windows_path_model, unix_path_model

TOTAL_ROUNDS = 16

class GameRound():
    def __init__(self):
        self.round = 0
        self.awards = get_awards()
        self.stop_round = self.get_stop_round()
        self.results =0
        self.final_award = np.sum(self.awards[0:16])

    def get_award_round(self):
        return self.awards[self.round]

    def get_round(self):
        return self.round

    def next_round(self):
        if self.round<self.stop_round:
            self.results += self.get_award_round()
            self.round += 1
            self.set_variables_label()
        else:
            round_label.set(0)
            results_label.set("You Lose!")
            awards_label.set(0)
            max_result_label.set(self.get_max_result())
            self.disabled_button()
            results_machine_label.set(np.sum(self.awards[0:self.get_machine_round()])) if self.get_machine_round()<self.stop_round else results_machine_label.set("Machine Lost")

    def get_machine_round(self):
        clp = pickle.load(open(windows_path_model, 'rb') if os.name == 'nt' else  open(
        unix_path_model, 'rb'))
        predicted = clp.predict(self.awards.reshape(1,-1))
        round_stop_machine = int(round(predicted[0]))
        return round_stop_machine

    def stop_game(self):
        max_result_label.set(self.get_max_result())
        self.disabled_button()
        machine_round = self.get_machine_round()
        if machine_round <self.stop_round:
            results_machine_label.set(np.sum(self.awards[0:machine_round]))
        else:
            results_machine_label.set("Machine Lose")

    def disabled_button(self):
        next_button.config(state='disabled')
        stop_button.config(state='disabled')

    def get_final_award(self):
        return self.final_award

    def restart(self):
        next_button.config(state='normal')
        stop_button.config(state='normal')
        self.round = 0
        self.awards = get_awards()
        self.stop_round = self.get_stop_round()
        self.results = 0
        self.final_award = np.sum(self.awards[0:16])
        self.set_variables_label()
        final_award_label.set(self.final_award)
        results_machine_label.set(0)
        max_result_label.set(0)


    def get_max_result(self):
        return np.sum(self.awards[0:self.stop_round])

    def set_variables_label(self):
        round_label.set(str(game.round) + "/16")
        results_label.set(self.results)
        awards_label.set(self.get_award_round())

    def get_stop_round(self):
        range_total_rounds = range(TOTAL_ROUNDS)
        for n in range_total_rounds:
            is_stop = self.is_stop_round(n)
            if n == len(range_total_rounds)-1:
                stop = n
                break
            if is_stop:
                stop = n
                break
        return stop

    def is_stop_round(self, n_round):
        per_rounds = TOTAL_ROUNDS-n_round
        round_choosen = np.random.randint(1,per_rounds)+1
        return round_choosen == per_rounds

def get_awards():
    award = 20+30*np.random.random_sample(16)
    np_sum = np.sum(award)
    final_award = np.concatenate((award, np.array([np_sum])))
    return final_award



def start_variables_gui():
    global round_label, awards_label, results_label, results_machine_label, final_award_label, max_result_label
    round_label = StringVar()
    awards_label = StringVar()
    results_label = StringVar()
    results_machine_label = StringVar()
    final_award_label = StringVar()
    max_result_label = StringVar()


def set_variables_gui():
    results_label.set(game.results)
    awards_label.set(game.get_award_round())
    round_label.set(str(game.get_round()) + "/16")
    final_award_label.set(game.get_final_award())


def create_buttons():
    global next_button, stop_button
    next_button = Button(command=game.next_round, text="Next Round")
    stop_button = Button(command=game.stop_game, text="Stop Game")
    Button(command=game.restart, text="New Game").grid(row=1, column=2)
    next_button.grid(row=1)
    stop_button.grid(row=1, column=1)


def create_labels():
    Label(root, text="Round").grid(row=0, column=0)
    Label(root, text="Total Award:").grid(row=0, column=2)
    Label(root, textvariable=round_label).grid(row=0, column=1)
    Label(root, textvariable=final_award_label).grid(row=0, column=3)
    Label(root, text="Award this round").grid(row=2, column=0)
    Label(root, textvariable=awards_label).grid(row=2, column=1)
    Label(root, text="Results").grid(row=3, column=0)
    Label(root, textvariable=results_label).grid(row=3, column=1)
    Label(root, text="Machine Win this:").grid(row=4, column=0)
    Label(root, textvariable=results_machine_label).grid(row=4, column=1)
    Label(root, text="Max Result").grid(row=5, column=0)
    Label(root, textvariable=max_result_label).grid(row=5, column=1)


if __name__ == "__main__":
    game = GameRound()
    root = Tk()
    root.title("Play Game!")
    start_variables_gui()
    set_variables_gui()
    create_buttons()
    create_labels()
    root.mainloop()

