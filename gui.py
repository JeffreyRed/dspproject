from tkinter import *
import matplotlib.pyplot as plt


def plot_test():
    z = [0, 1, 2, 3, 4, 5, 6, 7]
    plt.plot(z, z)
    plt.show()


class Gui:

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.lblList = []
        self.btnList = []
        self.window = Tk()
        self.window.geometry(str(self.width) + "x" + str(self.height))
        self.window.title(title)

    def create_button(self, text, function):
        self.btnList.append(Button(self.window, text=text, relief=RAISED, command=function).pack())

    def create_label(self, text):
        self.lblList.append(Label(self.window, text=text, font=("arial", 16, "bold")).pack())

    def create_window(self):
        self.load_window()

    def load_window(self):
        self.window.mainloop()
