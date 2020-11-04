from random import choice
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

class Person:

    def __init__(self, name):
        self.name = name
        self.greeting = 'Hello {name}'

    def __str__(self):
        return self.make_greeting()

    def make_greeting(self):
        return self.greeting.format(name=self.name)


def create_window():
    window = Tk()
    window.geometry("500x400")
    window.title("DSP Tool")
    label1 = Label(window, text="DSP Tool", font=("arial", 16, "bold")).pack()
    label2 = Label(window, text="Select the option you would like to use", font=("arial", 16)).pack()
    # label2 = Label(window, text="plot", font=("arial", 16)).place(x=10, y=60)
    plot_button = Button(window, text="PLOT", relief=RAISED, command=plot_test).pack()
    window.mainloop()


def plot_test():
    z = [0, 1, 2, 3, 4, 5, 6, 7]
    y = [0, 1, 2, 3, 4, 5, 6, 7]
    plt.plot(z, y)
    plt.show()


def main():
    people = [
        Person('1'),
        Person('2'),
        Person('3'),
    ]
    person = choice(people)
    print(person)
    create_window()


if __name__ == '__main__':
    main()
