from random import choice
import numpy as np
from gui import *
from audiocapture import *


class Person:

    def __init__(self, name):
        self.name = name
        self.greeting = 'Hello {name}'

    def __str__(self):
        return self.make_greeting()

    def make_greeting(self):
        return self.greeting.format(name=self.name)


def main():
    wn = Gui(400, 400, title="DSP Tool")
    wn.create_label("Choose one Option")
    wn.create_button("Plot", plot_test)
    wn.create_button("Record Audio", audio_capture)
    wn.load_window()


if __name__ == '__main__':
    main()
