from random import choice
import numpy as np
from gui import *
from audio import *
from rftool import *
from thinkdsp import read_wave
import matplotlib.pyplot as plt


def main():
    width = 800
    height = 400
    wn = Gui(width, height, title="DSP & RF Tool")
    # DSP Tool
    wn.create_label("Choose one Option for DSP", width/80, height/40)
    wn.create_button("Plot a Line (Demo Data)", plot_test, width/80, 50)
    wn.create_button("Record Audio Lib1", audio_capture, width/80, 100)
    wn.create_button("Record Audio Lib2 No file saved", audio_capture_opt2, width/80, 150)
    wn.create_button("Play Sound Output.wav", play_sound, width/80, 200)
    wn.create_button("Plot Audio File OutPut.wav", read_audio_file, width / 80, 250)
    # RF Tool
    wn.create_label("Choose one Option for RF", width / 2, height / 40)
    wn.create_button("Plot S Parameter from sp file", plot_demo_rf, width / 2, 50)
    wn.create_button("Plot load predefined", plot_three_load, width / 2, 100)
    wn.load_window()


if __name__ == '__main__':
    main()
