from collections import deque as dq
import numpy as np
from utils.dft_idft_dct import applyIDFT, applyDFT
import math


def correlation(magnitudes_1, magnitudes_2, periodic):
    # correlation with direct method
    N = len(magnitudes_1)
    results = []
    signal_2 = dq(magnitudes_2)  # double ended queue as it has rotate function making things easier
    if periodic:
        squared_sum_1 = sum(x * x for x in magnitudes_1)  #
        squared_sum_2 = sum(x * x for x in magnitudes_2)  # these lines calculate the normaliztion factor and here it is
        root = np.sqrt(squared_sum_1 * squared_sum_2)     # calculated once as it is periodic
        normalization_factor = round(root / N, 2)         #
        for i in range(N):
            result = 0
            for j in range(N):
                result += magnitudes_1[j] * signal_2[j]  # sum of x1(i) * x2(i)
            result /= N  # in the corr law
            result = round(result, 2)
            result /= normalization_factor  # to normalize
            results.append(round(result, 2))
            signal_2.rotate(-1)  # moving the first amp to the last position and shifting the rest

    else:
        for i in range(N):
            result = 0  # here normalization factor is calculated each time as it is non-periodic
            normalization_factor = round(
                np.sqrt(sum(x * x for x in magnitudes_1) * sum(x * x for x in magnitudes_2)) / N, 2)
            for j in range(N):
                result += magnitudes_1[j] * signal_2[j]
            result /= N
            result = round(result, 2)
            result /= normalization_factor
            results.append(round(result, 2))
            signal_2.rotate(-1)  # same as periodic but last element is 0 not the ex-first element
            signal_2[-1] = 0
    return results


def fast_correlation(magnitudes_1, magnitudes_2=None):
    # applying dft to both signals
    dft_mag1, dft_phase1 = applyDFT(magnitudes_1)
    if magnitudes_2 is not None:  # if a second signal is provided (cross correlation)
        dft_mag2, dft_phase2 = applyDFT(magnitudes_2)
    else:  # auto-correlation
        dft_mag2, dft_phase2 = dft_mag1, dft_phase1
    N = len(dft_mag1)
    real1 = []
    imag1 = []
    real2 = []
    imag2 = []
    # extracting real and imaginary parts
    for i in range(N):
        real1.append(dft_mag1[i] * math.cos(dft_phase1[i]))
        imag1.append(-(dft_mag1[i] * math.sin(dft_phase1[i])))  # - because of the conjugate
        real2.append(dft_mag2[i] * math.cos(dft_phase2[i]))
        imag2.append(dft_mag2[i] * math.sin(dft_phase2[i]))

    fd_mag = []
    fd_phases = []
    for i in range(N):  # multiplication of the 2 signals
        real = (real1[i] * real2[i]) - (imag1[i] * imag2[i])
        imag = (real1[i] * imag2[i]) + (real2[i] * imag1[i])
        fd_mag.append(math.sqrt(real ** 2 + imag ** 2))
        fd_phases.append(math.atan2(imag, real))

    idft = applyIDFT(fd_mag, fd_phases)  # applying IDFT to the result
    res = [round(x / N, 2) for x in idft]  # 1/N for the fast correlation law
    return res
