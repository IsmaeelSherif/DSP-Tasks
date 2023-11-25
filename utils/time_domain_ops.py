import numpy as np


def smooth(magnitudes, window):
    output = np.zeros(len(magnitudes))


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