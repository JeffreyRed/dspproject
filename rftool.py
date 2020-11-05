from skrf import Network, Frequency
import matplotlib.pyplot as plt


def plot_demo_rf():
    ring_slot = Network('ring slot.s2p')
    ring_slot.plot_s_smith()
    plt.show()
    plt.title("S-Parameters")


def plot_three_load():
    # dummy 2-port network from Frequency and s-parameters
    freq = Frequency(1, 10, 1, 'ghz')  # Frequency([start, stop, npoints, unit, …])
    print(freq)
    s = [0 + 1j, 0 - 1j, 0.23 - 0.43j]  # random complex numbers
    print(s)
    # if not passed, will assume z0=50. name is optional but it's a good practice.
    ntwk = Network(frequency=freq, z0=50, s=s, name='random values 1-port')
    print(ntwk)
    plt.figure()
    ntwk.plot_s_smith(marker='o', linestyle='dotted')
    plt.legend(loc=7)
    plt.text(0, 0.85, "0+1j", fontsize=12, bbox=dict(facecolor='red', alpha=0.5))
    plt.text(0, -0.85, "0-1j", fontsize=12, bbox=dict(facecolor='red', alpha=0.5))
    plt.text(0.28, -0.43, "0.23-0.43j", fontsize=12, bbox=dict(facecolor='red', alpha=0.5))
    plt.title("S-Parameters")
    plt.show()