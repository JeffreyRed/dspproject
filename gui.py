from tkinter import *
import matplotlib.pyplot as plt


def plot_test():
    x = [0, 1, 2, 3, 4, 5, 6, 7]
    plt.plot(x, x)
    plt.title('Demo Data')
    plt.xlabel('x')
    plt.ylabel('x')
    plt.show()


class Gui:

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.window = Tk()
        self.window.geometry(str(self.width) + "x" + str(self.height))
        self.window.title(title)

    def create_button(self, text, function, x, y):
        Button(self.window, text=text, relief=RAISED, command=function).place(x=x, y=y)

    def create_label(self, text, x, y):
        Label(self.window, text=text, font=("arial", 16, "bold")).place(x=x, y=y)

    def create_window(self):
        self.load_window()

    def load_window(self):
        self.window.mainloop()
