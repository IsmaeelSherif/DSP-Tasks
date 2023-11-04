import math
import numpy as np
from wave_drawer import draw_generalized

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


    amplitudes = [0] * N
    phases = [0] * N

    for i in range(N):
        real, imagine = calculateHarmonic(i)
        amplitudes[i] = math.sqrt( real ** 2 + imagine ** 2 )
        phases[i] = math.atan2(imagine, real)

    # to draw
    #fundemental_freq = (2 * math.pi) / (N * (1 / sampling_freq))
    #frequncies = np.arange(start=fundemental_freq, stop=N * fundemental_freq, step=fundemental_freq)
    #draw_generalized(frequncies, amplitudes, "frequncy", "amplitude")
    #draw_generalized(frequncies, phases, "frequncy", "phase")
    return amplitudes, phases

def applyIDFT(magnitudes,phase):
    N = len(magnitudes)
    amplitudes = []
    DFT_form = polar_to_complex(magnitudes,phase)
    for n in range(N) :
        value = 0
        for K in range(N):
            value += DFT_form[K] * (math.cos(2 * math.pi * K * n) +( complex(0 ,(1j * math.sin(2 * math.pi * K * n)))))
        value /= N
        amplitudes.append(value)
    x = np.arange(start=0, stop = N , step = 1 )
    draw_generalized(x , amplitudes , "n" , "amplitude")



