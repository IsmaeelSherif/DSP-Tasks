import math

import numpy as np


def applyDFT(magnitudes):

    N = len(magnitudes)

    def calculateHarmonic(k):
        realComponent = 0
        imaginaryComponent = 0
        for n in range(N):
            theta = (-2 * math.pi * k * n) / N
            realComponent += magnitudes[n] * math.cos(theta)
            imaginaryComponent += magnitudes[n] * math.sin(theta)
        return realComponent, round(imaginaryComponent , 4)


    amplitudes = []
    phases = []

    for i in range(N):
        real, imagine = calculateHarmonic(i)
        amplitudes.append( math.sqrt( real ** 2 + imagine ** 2 ))
        phases.append( math.atan2(imagine, real))

   
    return amplitudes, phases


def applyIDFT(amplitudes, phases):
    N = len(amplitudes)
    magnitudes = []
    for n in range(N):

        magnitude = 0

        for k in range(N):

            xReal = amplitudes[k] * math.cos(phases[k])
            xImagine = amplitudes[k] * math.sin(phases[k])

            theta = (2 * math.pi * k * n) / N
            eReal = math.cos(theta)
            eImagine = math.sin(theta)

            magnitude += eReal * xReal
            magnitude -= xImagine * eImagine

        magnitude = round(magnitude / N, 2)
        magnitudes.append(magnitude)
        
    return magnitudes

def applyDCT(magnitudes):
    N = len(magnitudes)
    coeffs = [0] * N

    for k in range(N):

        for n in range(N):
            theta = math.pi/(4*N)  * (2*n - 1) * (2*k - 1)
            coeffs[k] += magnitudes[n] * math.cos(theta)

        coeffs[k] = coeffs[k] * math.sqrt(2 / N)
        
    return coeffs

def remove_DC(magnitudes):
    N = len(magnitudes)
    mean = np.array(magnitudes).mean()
    new_mag = []
    for item in magnitudes:
        result = item - mean
        result = round(result, 3)
        print(result)
        new_mag.append(result)

    return new_mag
