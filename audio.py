import pyaudio
import wave
from tkinter import *
from tkinter import messagebox
import sounddevice as sd
import soundfile as sf
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from thinkdsp import read_wave
import matplotlib.pyplot as plt
from logcapture import *


def audio_capture():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    messagebox.showinfo("information", "Recording finished")
    data_log("Audio recorded as saved as output.wav")


def play_sound():
    filename = 'output.wav'
    # Extract data and sampling rate from file
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing
    data_log("play sound output.wav")


def audio_capture_opt2():
    fs = 44100
    duration = 5  # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2, dtype='float64')
    print("Recording Audio")
    sd.wait()
    print("Audio recording complete , Play Audio")
    sd.play(myrecording, fs)
    sd.wait()
    print("Play Audio Complete")
    data_log("using another method to record and play audio")


def read_audio_file():
    wave1 = read_wave("output.wav")
    start = 1.2
    duration = 0.6
    segment = wave1.segment(start, duration)
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Audio wave and spectrum')
    ax1.plot(segment.ts, segment.ys)
    # spectrum = segment.make_spectrum()
    spec = calculate_spectrum(wave1)
    ax2.plot(spec[0], spec[1])
    # plt.figure()
    # plt.plot(spectrum.fs, spectrum.amps)
    # plt.figure()
    # spectrum.plot()
    data_log("audio file read and played")
    plt.show()


def calculate_spectrum(wave_data):
    n = len(wave_data.ys)
    d = 1 / wave_data.framerate
    hs = abs(np.fft.fft(wave_data.ys))
    fs = np.fft.fftfreq(n, d)
    data_log("Spectrum Calculated")
    return fs, hs
