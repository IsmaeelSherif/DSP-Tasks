import math

def applyDFT(magnitudes):

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
    return amplitudes, phases