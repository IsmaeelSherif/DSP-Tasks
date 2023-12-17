import tkinter as tk
from utils.signal_reader import readInputFromFile
from models.signal import FDSignal, Signal
from testwave.Practical.Fast_Convolution.ConvTest import ConvTest
from utils.wave_drawer import draw_discrete
import utils.dft_idft_dct as freqOps
import math

def openFastConvDialog(root):

    inputSignal1 = None
    inputSignal2 = None

    def convFDSignals(amplitudes1, amplitudes2, phases1, phases2):
        N = len(amplitudes1)
        resMagnitudes = []
        resPhases = []
        for n in range(N):
            real1 = amplitudes1[n] * math.cos(phases1[n])
            imag1 = amplitudes1[n] * math.sin(phases1[n])

            real2 = amplitudes2[n] * math.cos(phases2[n])
            imag2 = amplitudes2[n] * math.sin(phases2[n])

            realRes = (real1 * real2) - (imag1 * imag2)
            imagRes = (real1 * imag2) + (real2 * imag1)

            resMag = math.sqrt( realRes ** 2 + imagRes ** 2 )
            resPhase = math.atan2(imagRes, realRes)

            resMagnitudes.append(resMag)
            resPhases.append(resPhase)

        return FDSignal(resMagnitudes, resPhases, '')


    def doConv() -> Signal:
        minX = min(min(inputSignal1.x), min(inputSignal2.x))
        maxX = max(max(inputSignal1.x), max(inputSignal2.x))
        resultX = list(range(int(minX), int(maxX) + 2))

        N1 = len(inputSignal1.magnitudes)
        N2 = len(inputSignal2.magnitudes)
        maxL = N1 + N2 - 1
        padded_list1 = inputSignal1.magnitudes + [0] * (maxL - N1)
        padded_list2 = inputSignal2.magnitudes + [0] * (maxL - N2)

        freq_domain_1, phases1 = freqOps.applyDFT(padded_list1)
        freq_domain_2, phases2 = freqOps.applyDFT(padded_list2)

        convResult = convFDSignals(freq_domain_1, freq_domain_2, phases1, phases2)

        idft = freqOps.applyIDFT(convResult.amplitudes, convResult.phaseShifts)

        return Signal(resultX, idft, 'y(n)')


    def onButtonPress():
        if isinstance(inputSignal1, Signal) and isinstance(inputSignal2, Signal):

            result = doConv()
            ConvTest(result.x, result.magnitudes)
            draw_discrete(result.x, result.magnitudes , "y(n)" , "magnitude")



    def change_label_text(label):
        nonlocal inputSignal1
        inputSignal1 = readInputFromFile('testwave/Practical/Fast_Convolution')
        if(inputSignal1):
            label.config(text=inputSignal1.fileName)

    
    def change_label_text2(label):
        nonlocal inputSignal2
        inputSignal2 = readInputFromFile('testwave/Task7')
        if(inputSignal2):
            label.config(text=inputSignal2.fileName)


    
    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Signal Fast Convolution")
    dialog.geometry("360x300")



    # Create a frame for the components
    frame = tk.Frame(dialog, padx=10, pady=10)
    frame.pack()
    
    button1 = tk.Button(frame, text="X(n)", command=lambda: change_label_text(label1))
    button1.grid(row=0, column=0, padx=5)
    label1 = tk.Label(frame, text="")
    label1.grid(row=0, column=1)

    button2 = tk.Button(frame, text="H(n)", command=lambda: change_label_text2(label2))
    button2.grid(row=2, column=0, padx=5)
    label2 = tk.Label(frame, text="")
    label2.grid(row=2, column=1)

    
    # Button
    show_button = tk.Button(frame, text="Conv", command=onButtonPress)
    show_button.grid(row=3, column=0, columnspan=2, pady=10)

    dialog.wait_window()