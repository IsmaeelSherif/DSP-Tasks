import tkinter as tk
from utils.signal_reader import readInputFromFile
from utils.signal_exporter import exportSignalToFile
from utils.dft_idft_dct import applyDFT, applyIDFT, applyDCT , remove_DC
from testwave.Task4.signalcompare import SignalComapreAmplitude, SignalComaprePhaseShift
from testwave.comparesignals import compareSignalToFile
from dialogs.edit_signal import openEditDialog
from utils.wave_drawer import draw_discrete
from models.signal import Signal, FDSignal
import numpy as np
import math

def openFreqDomainDialog(root):

    inputSignal = None


    def change_label_text(label):
        nonlocal inputSignal
        inputSignal = readInputFromFile('testwave/Task5')
        if(inputSignal):
            label.config(text=inputSignal.fileName)


    def export():
        filePath = 'testwave/Task5/exported.txt'
        if(inputSignal):
            if(isinstance(inputSignal, Signal)):
                maxLength = len(inputSignal.magnitudes)
                try:
                    maxLength = int(export_textbox.get())
                except:
                    pass
                inputSignal.x = range(maxLength)
                inputSignal.magnitudes = inputSignal.magnitudes[0 : maxLength]

            exportSignalToFile(inputSignal, filePath)


    def drawCurrentSignal():
        if inputSignal:
            if isinstance(inputSignal, Signal):
                draw_discrete(inputSignal.x, inputSignal.magnitudes , "samples (n)" , "amplitude")
            else:
                samplingFreq = 0
                try:
                    samplingFreq = float(factor_textbox.get())
                except:
                    print('Put a correct sampling frequency')
                    return
                draw_DFT(inputSignal.amplitudes, inputSignal.phaseShifts, samplingFreq)


    def draw_DFT(amplitudes, phases, samplingFreq):
        N = len(amplitudes)
        fundemental_freq = (2 * math.pi) / (N * (1 / samplingFreq))
        frequncies = np.arange(start = fundemental_freq , stop = (N+1) * fundemental_freq, step = fundemental_freq)
        for i in range(len(frequncies)):
            frequncies[i] = round(frequncies[i],3)
            
        phases_degree = []
        for item in phases :
            value = item * (180 / math.pi)
            phases_degree.append(value)
        draw_discrete(frequncies, amplitudes, "frequncy", "amplitude")
        draw_discrete(frequncies, phases_degree, "frequncy", "phase (degree)")

    def edit():
        if(inputSignal and isinstance(inputSignal, FDSignal)):
            new_amps, new_phases = openEditDialog(dialog, inputSignal.amplitudes, inputSignal.phaseShifts)
            inputSignal.amplitudes = new_amps
            inputSignal.phaseShifts = new_phases
            

    def testDFT():
        nonlocal inputSignal
        if(inputSignal and isinstance(inputSignal, Signal)):

            samplingFreq = 0
            try:
                samplingFreq = float(factor_textbox.get())
            except:
                print('Put a correct sampling frequency')
                return
        
            amplitudes, phases = applyDFT(inputSignal.magnitudes)
            inputSignal = FDSignal(amplitudes, phases, 'custom FD Signal')

            actualOutputSignal = readInputFromFile('testwave/Task4')
            if actualOutputSignal:
                print('SignalComapreAmplitude', SignalComapreAmplitude(actualOutputSignal.amplitudes, amplitudes))
                print('SignalComaprePhaseShift', SignalComaprePhaseShift(actualOutputSignal.phaseShifts, phases))
            draw_DFT(amplitudes, phases, samplingFreq)
            label1.config(text=inputSignal.fileName)


    

    def testIDFT():
        nonlocal inputSignal
        if(inputSignal and isinstance(inputSignal, FDSignal)):
            magnitudes = applyIDFT(inputSignal.amplitudes, inputSignal.phaseShifts)
            x = range(len(magnitudes))
            inputSignal = Signal(x, magnitudes, 'custom TD Signal')
            label1.config(text=inputSignal.fileName)
            compareSignalToFile(magnitudes)
            draw_discrete(x, magnitudes , "samples (n)" , "amplitude")

    def testDCT():
        nonlocal inputSignal
        if(inputSignal and isinstance(inputSignal, Signal)):
            magnitudes = applyDCT(inputSignal.magnitudes)
            x = range(len(magnitudes))
            inputSignal = Signal(x, magnitudes, 'custom DCT Signal')
            label1.config(text=inputSignal.fileName)
            compareSignalToFile(magnitudes)
            draw_discrete(x, magnitudes , "samples (n)" , "DCT")

    def remove_DC_component():
        nonlocal inputSignal
        if inputSignal and isinstance(inputSignal, Signal):
            inputSignal.magnitudes = remove_DC(inputSignal.magnitudes)
            compareSignalToFile(inputSignal.magnitudes)
            draw_discrete(inputSignal.x, inputSignal.magnitudes, "samples (n)", "amplitude")

    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Frequency Domain")
    dialog.geometry("360x300")

    # Create a frame for the buttons and labels
    button_frame = tk.Frame(dialog, padx=10, pady=10)
    button_frame.pack()

    # Button 1
    button1 = tk.Button(button_frame, text="Input Signal", command=lambda: change_label_text(label1))
    button1.grid(row=0, column=0, pady=5, padx=5)
    label1 = tk.Label(button_frame, text="")
    label1.grid(row=0, column=1)

    factor_label = tk.Label(dialog, text="Sampling Frequency")
    factor_label.pack()

    factor_textbox = tk.Entry(dialog)
    factor_textbox.pack()

    button_frame2 = tk.Frame(dialog, padx=10, pady=10)
    button_frame2.pack()

    idft_btn = tk.Button(button_frame2, text="test IDFT", command=testIDFT)
    idft_btn.grid(row=0, column=0, padx=5)

    dft_btn = tk.Button(button_frame2, text="test DFT", command=testDFT)
    dft_btn.grid(row=0, column=1, padx=5)

    dct_btn = tk.Button(button_frame2, text="test DCT", command=testDCT)
    dct_btn.grid(row=0, column=2, padx=5)

    editBtn = tk.Button(dialog, text="edit signal", command=edit)
    editBtn.pack(pady=5)

#DC button
    button_frame3 = tk.Frame(dialog, padx=10, pady=10)  # Added frame for the new button
    button_frame3.pack()

    # Added button to remove DC component
    remove_DC_btn = tk.Button(button_frame3, text="Remove DC Component", command=remove_DC_component)
    remove_DC_btn.grid(row=0, column=0, pady=5, padx=5)



    showBtn = tk.Button(dialog, text="show signal", command=drawCurrentSignal)
    showBtn.pack(pady=5)

    export_frame = tk.Frame(dialog)  # Create a frame for exportBtn and textbox
    export_frame.pack()

    exportBtn = tk.Button(export_frame, text="export signal", command=export)
    exportBtn.pack(side=tk.LEFT, padx=5)

    export_textbox = tk.Entry(export_frame)
    export_textbox.pack(side=tk.LEFT, padx=5)