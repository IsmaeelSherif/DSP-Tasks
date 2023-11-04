import tkinter as tk
from utils.signal_reader import readInputFromFile
from utils.signal_exporter import exportSignalToFile
from utils.dft_idft import applyDFT, applyIDFT
from testwave.Task4.signalcompare import SignalComapreAmplitude, SignalComaprePhaseShift
from dialogs.edit_signal import openEditDialog

def openFreqDomainDialog(root):

    inputSignal = None


    def change_label_text(label):
        nonlocal inputSignal
        inputSignal = readInputFromFile('testwave/Task4')
        if(inputSignal):
            label.config(text=inputSignal.fileName)

    def calculateResult():
        samplingFreq = 0
        try:
            samplingFreq = float(factor_textbox.get())
        except:
            print('Put a correct sampling frequency')
            return


    def export():
        exportSignalToFile('testwave/Task4/exported.txt')

    def edit():
        if(inputSignal):
            amplitudes, phases = applyDFT(inputSignal.magnitudes , )
            new_amps, new_phases = openEditDialog(dialog, amplitudes, phases)
            print('newAmps', new_amps)
            print('newPhases', new_phases)
            

    def testDFT():
        if(inputSignal):
            amplitudes, phases = applyDFT(inputSignal.magnitudes ,int(factor_textbox.get()) )
            actualOutputSignal = readInputFromFile('testwave/Task4')
            print('SignalComapreAmplitude', SignalComapreAmplitude(actualOutputSignal.amplitudes, amplitudes))
            print('SignalComaprePhaseShift', SignalComaprePhaseShift(actualOutputSignal.phaseShifts, phases))

    def testIDFT():
        if(inputSignal):
            magnitudes = applyIDFT(inputSignal.amplitudes, inputSignal.phaseShifts)
            # print('SignalComapreAmplitude', SignalComapreAmplitude(actualOutputSignal.amplitudes, amplitudes))
            # print('SignalComaprePhaseShift', SignalComaprePhaseShift(actualOutputSignal.phaseShifts, phases))
            

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

    show_button = tk.Button(button_frame2, text="test IDFT", command=testIDFT)
    show_button.grid(row=0, column=0, padx=5)

    compare_button = tk.Button(button_frame2, text="test DFT", command=testDFT)
    compare_button.grid(row=0, column=1, padx=5)

    editBtn = tk.Button(dialog, text="edit signal", command=edit)
    editBtn.pack(pady=5)

    exportBtn = tk.Button(dialog, text="export signal", command=export)
    exportBtn.pack(pady=5)

    dialog.wait_window()