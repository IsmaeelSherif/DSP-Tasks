import tkinter as tk
from utils.signal_reader import readInputFromFile
from models.signal import Signal
from testwave.Task7.ConvTest import ConvTest
from utils.wave_drawer import draw_discrete

def openConvDialog(root):

    inputSignal1 = None
    inputSignal2 = None


    def doConv() -> Signal:
        minX = min(min(inputSignal1.x), min(inputSignal2.x))
        maxX = max(max(inputSignal1.x), max(inputSignal2.x))
        resultX = list(range(int(minX), int(maxX) + 2))
        magnitudes = [0] * len(resultX)

        for n in range(len(resultX)):
            for k in range(len(inputSignal2.x)):
                if n - k >= 0 and n - k < len(inputSignal1.x):
                    magnitudes[n] += inputSignal1.magnitudes[n - k] * inputSignal2.magnitudes[k]

        return Signal(resultX, magnitudes, 'y(n)')




    def onButtonPress():
        if isinstance(inputSignal1, Signal) and isinstance(inputSignal2, Signal):
            result = doConv()
            ConvTest(result.x, result.magnitudes)
            draw_discrete(result.x, result.magnitudes , "y(n)" , "magnitude")



    def change_label_text(label):
        nonlocal inputSignal1
        inputSignal1 = readInputFromFile('testwave/Task7')
        if(inputSignal1):
            label.config(text=inputSignal1.fileName)

    
    def change_label_text2(label):
        nonlocal inputSignal2
        inputSignal2 = readInputFromFile('testwave/Task7')
        if(inputSignal2):
            label.config(text=inputSignal2.fileName)


    
    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Signal Convolution")
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