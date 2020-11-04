from random import choice
import numpy as np
from gui import *
from audio import *


def main():
    wn = Gui(400, 400, title="DSP Tool")
    wn.create_label("Choose one Option")
    wn.create_button("Plot", plot_test)
    wn.create_button("Record Audio", audio_capture)
    wn.create_button("Play Sound", play_sound)
    wn.load_window()


if __name__ == '__main__':
    main()
