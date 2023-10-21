import tkinter as tk
from tkinter import scrolledtext
from utils import wave_drawer
from utils.example_reader import readInputFromFile
from utils import arithmetic_ops
from testwave.comparesignals import compareSignalToFile

def openMultiplyDialog(root):

    inputSignal = None




    def change_label_text(label):
        nonlocal inputSignal
        inputSignal, displayName = readInputFromFile()
        if(inputSignal):
            label.config(text=displayName)


    def show():
        if(inputSignal):
            result = calculateResult()
            if(result):
                wave_drawer.draw(result)

    def compare():
        if(inputSignal):
            result = calculateResult()
            if(result):
                compareSignalToFile(result)

    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Signal Multiplication")
    dialog.geometry("360x300")

    # Create a frame for the buttons and labels
    button_frame = tk.Frame(dialog, padx=10, pady=10)
    button_frame.pack()

    # Button 1
    button1 = tk.Button(button_frame, text="Input Signal", command=lambda: change_label_text(label1))
    button1.grid(row=0, column=0, pady=5, padx=5)
    label1 = tk.Label(button_frame, text="")
    label1.grid(row=0, column=1)



    factor_label = tk.Label(dialog, text="Factor")
    factor_label.pack()

    factor_textbox = tk.Entry(dialog)
    factor_textbox.pack()

    button_frame2 = tk.Frame(dialog, padx=10, pady=10)
    button_frame2.pack()

    def calculateResult():
        factor = 0
        try:
            factor = float(factor_textbox.get())
        except:
            print('Put a correct Factor')
            return
        nonlocal inputSignal
        multiplyRes = arithmetic_ops.multiplyWave(inputSignal, factor)
        return multiplyRes

    show_button = tk.Button(button_frame2, text="Show", command=show)
    show_button.grid(row=0, column=0, padx=5)

    compare_button = tk.Button(button_frame2, text="Compare", command=compare)
    compare_button.grid(row=0, column=1, padx=5)

    dialog.wait_window()