import tkinter as tk
from tkinter.filedialog import askopenfilename
from utils.signal_reader import readInputFromFile_2
from utils.correlation import fast_correlation
from utils.wave_drawer import draw_discrete
import numpy as np
from models.signal import Signal
from testwave.Practical.Fast_Correlation.CompareSignal import Compare_Signals

def openFastCorrelationDialog(root):
    signal_1 = None
    signal_2 = None

    def fast_correlate() -> Signal:
        nonlocal signal_1, signal_2  # Use nonlocal instead of global
        if isinstance(signal_1, Signal):
            magnitudes_1 = signal_1.magnitudes
            magnitudes_2 = None

            if isinstance(signal_2, Signal):
                magnitudes_2 = signal_2.magnitudes

            # Call the fast_correlation function with the magnitudes
            result = fast_correlation(magnitudes_1, magnitudes_2)

            # Display or use the result as needed
            print(result)
            Compare_Signals(
                "C:\\Users\\Adham Ebaid\\Desktop\\college\\second to last semester\\DSP\\Lab_work\\DSP-Tasks\\testwave\\Practical\\Fast_Correlation\\Corr_Output.txt",
                np.arange(start=0, stop=4, step=1), result)
            draw_discrete(np.arange(start=0, stop=len(result), step=1), result, "n", "amplitude")

    def change_label_text(label):
        nonlocal signal_1
        signal_1 = readInputFromFile_2('testwave/Practical/Fast_Correlation')
        if signal_1:
            label.config(text=signal_1.fileName)

    def change_label_text2(label):
        nonlocal signal_2
        signal_2 = readInputFromFile_2('testwave/Practical/Fast_Correlation')
        if signal_2:
            label.config(text=signal_2.fileName)

    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Fast Correlation Dialog")
    dialog.geometry("360x300")

    # Create a frame for the components
    frame = tk.Frame(dialog, padx=10, pady=10)
    frame.pack()

    button1 = tk.Button(frame, text="Signal 1", command=lambda: change_label_text(label1))
    button1.grid(row=0, column=0, padx=5)
    label1 = tk.Label(frame, text="")
    label1.grid(row=0, column=1)

    button2 = tk.Button(frame, text="Signal 2", command=lambda: change_label_text2(label2))
    button2.grid(row=2, column=0, padx=5)
    label2 = tk.Label(frame, text="")
    label2.grid(row=2, column=1)

    # Button
    correlate_button = tk.Button(frame, text="Fast Correlate", command=fast_correlate)
    correlate_button.grid(row=3, column=0, columnspan=2, pady=10)

    dialog.wait_window()
