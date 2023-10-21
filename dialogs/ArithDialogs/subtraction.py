import tkinter as tk
from tkinter import scrolledtext
from utils import wave_drawer
from utils.signal_reader import readInputFromFile
from utils import arithmetic_ops
from testwave.comparesignals import compareSignalToFile

def openSubDialog(root):

    signal1 = None
    signal2 = None

    def change_label_text(signalNum, label):
        inputSignal = readInputFromFile()
        if(inputSignal):
            if(signalNum == 1):
                nonlocal signal1
                signal1 = inputSignal
            else:
                nonlocal signal2
                signal2 = inputSignal
            label.config(text=inputSignal.fileName)


    def show():
        result = arithmetic_ops.subWave(signal1, signal2)
        print('Sub result', result)
        x = range(0, len(result))
        wave_drawer.draw(x, result)

    def compare():
        result = arithmetic_ops.subWave(signal1, signal2)
        print('Sub result', result)
        compareSignalToFile(result)

    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Signal Subtraction")
    dialog.geometry("360x300")

    minus = tk.Label(dialog, text="Signal 1 - Signal 2")
    minus.pack()

    # Create a frame for the buttons and labels
    button_frame = tk.Frame(dialog, padx=10, pady=10)
    button_frame.pack()

    # Button 1
    button1 = tk.Button(button_frame, text="Signal 1", command=lambda: change_label_text(1, label1))
    button1.grid(row=0, column=0, pady=5, padx=5)
    label1 = tk.Label(button_frame, text="")
    label1.grid(row=0, column=1)



    # Button 2
    button2 = tk.Button(button_frame, text="Signal 2", command=lambda: change_label_text(2, label2))
    button2.grid(row=1, column=0, pady=5, padx=5)
    label2 = tk.Label(button_frame, text="")
    label2.grid(row=1, column=1)

    button_frame2 = tk.Frame(dialog, padx=10, pady=10)
    button_frame2.pack()

    show_button = tk.Button(button_frame2, text="Show", command=show)
    show_button.grid(row=0, column=0, padx=5)

    compare_button = tk.Button(button_frame2, text="Compare", command=compare)
    compare_button.grid(row=0, column=1, padx=5)

    dialog.wait_window()