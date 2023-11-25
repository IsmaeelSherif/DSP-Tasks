import tkinter as tk
from tkinter.filedialog import askopenfilename
from utils.signal_reader import readInputFromFile
import testwave.Task6.Derivative.DerivativeSignal as DerrTest
from testwave.Task6.Shifting_Folding.Shift_Fold_Signal import Shift_Fold_Signal
import utils.time_domain_ops as ops
import utils.arithmetic_ops as arithOps
from utils.wave_drawer import draw_discrete
from models.signal import Signal, FDSignal
import numpy as np
import math

def openTimeDomainDialog(root):

    inputSignal = None


    def change_label_text(label):
        nonlocal inputSignal
        inputSignal = readInputFromFile('testwave/Task6')
        if(inputSignal):
            label.config(text=inputSignal.fileName)


    def getWindowSize():
        try:
            window = int(factor_textbox.get())
            return window
        except:
            raise('Put a correct sampling frequency')
        

    def smooth():
        nonlocal inputSignal
        if inputSignal:
            if isinstance(inputSignal, Signal):
                window = getWindowSize()
                smoothed = ops.smooth(inputSignal.magnitudes,window)
                print(smoothed)
                x = np.arange(start= 0 , stop = len(smoothed) , step = 1)
                draw_discrete(x , smoothed , "sample","amplitude")

    def removeDC():
        nonlocal inputSignal
        if inputSignal:
            if isinstance(inputSignal, Signal):
                result = ops.remove_dc_freq(inputSignal.magnitudes)
                print(result)
                x = np.arange(start=0, stop=len(result), step=1)
                draw_discrete(x, result, "sample", "amplitude")


    def sharpen():
        inputSignalMag = DerrTest.InputSignal
        firstDerr, SecondDerr = ops.sharpen(inputSignalMag)
        DerrTest.DerivativeSignal(firstDerr, SecondDerr)


    def fold():
        nonlocal inputSignal
        if inputSignal:
            if isinstance(inputSignal, Signal):
                folded = ops.fold(inputSignal.magnitudes)
                
                test_output_file_path = askopenfilename(initialdir='testwave/Task6/Shifting_Folding')

                Shift_Fold_Signal(test_output_file_path, inputSignal.x, folded)
                    
                inputSignal = Signal(inputSignal.x, folded, 'folded TD Signal')
                label1.config(text=inputSignal.fileName)

    def delay():
        nonlocal inputSignal
        if inputSignal:
            if isinstance(inputSignal, Signal) and ('folded' in inputSignal.fileName):

                k = getWindowSize()
                delayedSignal = arithOps.shiftWave(inputSignal, -k)
                
                test_output_file_path = askopenfilename(initialdir='testwave/Task6/Shifting_Folding')

                Shift_Fold_Signal(test_output_file_path, delayedSignal.x, delayedSignal.magnitudes)
                    
                inputSignal = Signal(delayedSignal.x, delayedSignal.magnitudes, 'shift-folded TD Signal')
                label1.config(text=inputSignal.fileName)


    def drawCurrentSignal():
        if inputSignal:
            if isinstance(inputSignal, Signal):
                draw_discrete(inputSignal.x, inputSignal.magnitudes , "samples (n)" , "amplitude")




    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Time Domain")
    dialog.geometry("360x300")

    # Create a frame for the buttons and labels
    button_frame = tk.Frame(dialog, padx=10, pady=10)
    button_frame.pack()

    # Button 1
    button1 = tk.Button(button_frame, text="Input Signal", command=lambda: change_label_text(label1))
    button1.grid(row=0, column=0, pady=5, padx=5)
    label1 = tk.Label(button_frame, text="")
    label1.grid(row=0, column=1)

    factor_label = tk.Label(dialog, text="(k) steps")
    factor_label.pack()

    factor_textbox = tk.Entry(dialog)
    factor_textbox.pack()

    button_frame2 = tk.Frame(dialog, padx=10, pady=10)
    button_frame2.pack()

    idft_btn = tk.Button(button_frame2, text="Smooth", command=smooth)
    idft_btn.grid(row=0, column=0, padx=5)

    dft_btn = tk.Button(button_frame2, text="Delay", command=delay)
    dft_btn.grid(row=0, column=1, padx=5)

    button_frame3 = tk.Frame(dialog, padx=10, pady=10)
    button_frame3.pack()

    sharpBtn = tk.Button(button_frame3, text="Test Derrive", command=sharpen)
    sharpBtn.grid(row=0, column=0, padx=5)

    foldBtn = tk.Button(button_frame3, text="Fold", command=fold)
    foldBtn.grid(row=0, column=1, padx=5)

#DC button
    button_frame3 = tk.Frame(dialog, padx=10, pady=10)  # Added frame for the new button
    button_frame3.pack()

    # Added button to remove DC component
    remove_DC_btn = tk.Button(button_frame3, text="Remove DC Component", command=removeDC)
    remove_DC_btn.grid(row=0, column=0, pady=5, padx=5)



    showBtn = tk.Button(dialog, text="show signal", command=drawCurrentSignal)
    showBtn.pack(pady=5)