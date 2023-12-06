import tkinter as tk
from tkinter.filedialog import askopenfilename
from utils.signal_reader import readInputFromFile
from utils.correlation import correlation
from utils.wave_drawer import draw_discrete
import numpy as np
from models.signal import Signal


def openCorrelationDialog(root):
    signal_1 = None
    signal_2 = None

    def correlate() -> Signal:
        if isinstance(signal_1, Signal) and isinstance(signal_2, Signal):
            magnitudes_1 = signal_1.magnitudes
            magnitudes_2 = signal_2.magnitudes
            is_periodic = periodic_var.get()  # Use get() on the associated variable

            # Call the correlation function with the magnitudes and periodicity information
            result = correlation(magnitudes_1, magnitudes_2, is_periodic)

            # Display or use the result as needed
            print(result)
            draw_discrete(np.arange(start=0, stop=len(result), step=1), result, "n", "amplitude")

    def change_label_text(label):
        nonlocal signal_1
        signal_1 = readInputFromFile('testwave/task 8')
        if (signal_1):
            label.config(text=signal_1.fileName)

    def change_label_text2(label):
        nonlocal signal_2
        signal_2 = readInputFromFile('testwave/task 8')
        if (signal_2):
            label.config(text=signal_2.fileName)

    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Signal Correlation")
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

    # Checkbox
    periodic_var = tk.BooleanVar()  # Use BooleanVar to associate with the Checkbox
    periodic_checkbox = tk.Checkbutton(frame, text="Periodic", variable=periodic_var, onvalue=True, offvalue=False)
    periodic_checkbox.grid(row=3, column=0, columnspan=2, pady=5)

    # Button
    correlate_button = tk.Button(frame, text="Correlate", command=correlate)
    correlate_button.grid(row=4, column=0, columnspan=2, pady=10)

    dialog.wait_window()
