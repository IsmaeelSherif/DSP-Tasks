import math
import numpy as np
from utils.wave_drawer import draw_generalized , draw_discrete
from decimal import Decimal, getcontext


def export_to_text(array1, array2, file_path):
    if len(array1) == len(array2):
        with open(file_path, 'w') as file:
            for i in range(len(array1)):
                line = f"{array1[i]}, {array2[i]}\n"
                file.write(line)

def polar_to_complex(magnitudes, phases):
    complex_components = []
    for mag, phase in zip(magnitudes, phases):
        value = complex( ( mag * np.cos(phase)), (1j * np.sin(phase)))
        complex_components.append(value)

    return complex_components

def applyDFT(magnitudes , sampling_freq):

    N = len(magnitudes)

    def calculateHarmonic(k):
        realComponent = 0
        imaginaryComponent = 0
        for n in range(N):
            theta = (-2 * math.pi * k * n) / N
            realComponent += magnitudes[n] * math.cos(theta)
            imaginaryComponent += magnitudes[n] * math.sin(theta)
        #     print('add sin', n * math.sin(theta))
        #     print('add cos', n * math.cos(theta))
        # print(k, 'final real-imag', realComponent, imaginaryComponent)
        return realComponent, round(imaginaryComponent , 4)


    amplitudes = []
    phases = []

    for i in range(N):
        real, imagine = calculateHarmonic(i)
        amplitudes.append( math.sqrt( real ** 2 + imagine ** 2 ))
        phases.append( math.atan2(imagine, real))

    # to draw
    fundemental_freq = round( (2 * math.pi) / (N * (1 / sampling_freq)),3)
    frequncies = np.arange(start = fundemental_freq , stop = round(((N+1) * fundemental_freq),3), step= round(fundemental_freq,3))
    for item in frequncies:
        item = round(item,3)
    #for i in frequncies:
        #print(i)
    phases_degree = []
    for item in phases :
        value = item * (180 / math.pi)
        phases_degree.append(value)
    draw_discrete(frequncies, amplitudes, "frequncy", "amplitude")
    draw_discrete(frequncies, phases_degree, "frequncy", "phase (degree)")
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
        print('n', n, magnitude)
    x_axis = np.arange(start=0, stop=N, step=1)
    draw_discrete(x_axis, magnitudes , "samples (n)" , "amplitude")
    # DFT_form = polar_to_complex(magnitudes,phase)
    # for n in range(N) :
    #     value = 0
    #     for K in range(N):
    #         value += DFT_form[K] * (math.cos(2 * math.pi * K * n) +( complex(0 ,(1j * math.sin(2 * math.pi * K * n)))))
    #     value /= N
    #     amplitudes.append(value)
    # x = np.arange(start=0, stop = N , step = 1 )
    # draw_generalized(x , amplitudes , "n" , "amplitude")



