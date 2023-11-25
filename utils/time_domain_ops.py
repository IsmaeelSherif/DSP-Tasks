import numpy as np
from utils.dft_idft_dct import applyDFT , applyIDFT

def smooth(magnitudes, window):
    N = len(magnitudes)
    padded_magnitudes = []
    padded_N = N + (2*window)
    for i in range(padded_N):
        if i < window or i >= (N+window):
            padded_magnitudes.append(0)
        else:
            padded_magnitudes.append(magnitudes[i-window])
    iterator = window
    smoothed_magnitudes = []
    while iterator < (N+window):
        accumulator = 0
        for i in range(iterator-window,(iterator+window)+1):
            accumulator += padded_magnitudes[i]
        accumulator = accumulator/((2*window)+1)
        smoothed_magnitudes.append(round(accumulator,2))
        iterator += 1
    return smoothed_magnitudes


def sharpen(magnitudes):
    firstDerr = np.zeros(len(magnitudes) - 1)

    for i in range(1, len(magnitudes)):
        firstDerr[i-1] = magnitudes[i] - magnitudes[i-1]


    secondDerr = np.zeros(len(firstDerr) - 1)

    for i in range(1, len(firstDerr)):
        secondDerr[i-1] = magnitudes[i+1] - (2 * magnitudes[i]) + magnitudes[i-1]

    return firstDerr, secondDerr



def fold(magnitudes):
    return magnitudes[::-1]

#Task 6
def remove_dc_freq(magnitudes):
    N = len(magnitudes)
    amplitudes,phases = applyDFT(magnitudes)
    amplitudes[0] = 0
    phases[0] = 0
    new_magnitudes = applyIDFT(amplitudes,phases)
    return new_magnitudes