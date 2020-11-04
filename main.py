from random import choice
import numpy as np
from gui import *
from audio import *
from thinkdsp import read_wave
import matplotlib.pyplot as plt


def main():
    width = 400
    height = 400
    wn = Gui(width, height, title="DSP Tool")
    wn.create_label("Choose one Option", width/4, height/40)
    wn.create_button("Plot a Line (Demo Data)", plot_test, width/4, 50)
    wn.create_button("Record Audio Lib1", audio_capture, width/4, 100)
    wn.create_button("Record Audio Lib2 No file saved", audio_capture_opt2, width/4, 150)
    wn.create_button("Play Sound Output.wav", play_sound, width/4, 200)
    wn.create_button("Plot Audio File OutPut.wav", read_audio_file, width / 4, 250)
    wn.load_window()


if __name__ == '__main__':
    main()
