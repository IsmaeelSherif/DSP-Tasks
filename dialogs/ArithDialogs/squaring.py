import tkinter as tk
from utils import wave_drawer
from utils.signal_reader import readInputFromFile
from utils import arithmetic_ops
from testwave.comparesignals import compareSignalToFile

def openSquaringDialog(root):

    squaredSignal = None



    def change_label_text(label):
        inputSignal = readInputFromFile()
        if(inputSignal):
            label.config(text=inputSignal.fileName)
            nonlocal squaredSignal
            squaredSignal = arithmetic_ops.squarWave(inputSignal)


    def show():
        if(squaredSignal):
            x = range(0, len(squaredSignal))
            wave_drawer.draw(x, squaredSignal)

    def compare():
        if(squaredSignal):
            compareSignalToFile(squaredSignal)

    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Signal Squaring")
    dialog.geometry("360x300")

    # Create a frame for the buttons and labels
    button_frame = tk.Frame(dialog, padx=10, pady=10)
    button_frame.pack()

    # Button 1
    button1 = tk.Button(button_frame, text="Input Signal", command=lambda: change_label_text(label1))
    button1.grid(row=0, column=0, pady=5, padx=5)
    label1 = tk.Label(button_frame, text="")
    label1.grid(row=0, column=1)


    button_frame2 = tk.Frame(dialog, padx=10, pady=10)
    button_frame2.pack()


    show_button = tk.Button(button_frame2, text="Show", command=show)
    show_button.grid(row=0, column=0, padx=5)

    compare_button = tk.Button(button_frame2, text="Compare", command=compare)
    compare_button.grid(row=0, column=1, padx=5)

    dialog.wait_window()