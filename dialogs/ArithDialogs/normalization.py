import tkinter as tk
from utils import wave_drawer
from utils.signal_reader import readInputFromFile
from utils import arithmetic_ops
from testwave.comparesignals import compareSignalToFile

def openNormalizeDialog(root):

    inputSignal = None
    # Create a IntVar to store the selected type
    selected_type = tk.IntVar(value=0)


    def change_label_text(label):
        nonlocal inputSignal
        inputSignal = readInputFromFile()
        if(inputSignal):
            label.config(text=inputSignal.fileName)


    def show():
        if(inputSignal):
            result = calculateResult()
            x = range(0, len(result))
            wave_drawer.draw(x, result)

    def compare():
        if(inputSignal):
            result = calculateResult()
            compareSignalToFile(result)
                
    def calculateResult():
        choice = selected_type.get()
        nonlocal inputSignal
        normalizeRes = arithmetic_ops.normalizeWave(inputSignal, choice)
        return normalizeRes
    
    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Signal Normalization")
    dialog.geometry("360x300")




    # Create a frame for the components
    frame = tk.Frame(dialog, padx=10, pady=10)
    frame.pack()
    

    button1 = tk.Button(frame, text="Input Signal", command=lambda: change_label_text(label1))
    button1.grid(row=0, column=0, padx=5)
    label1 = tk.Label(frame, text="")
    label1.grid(row=0, column=1)
    
    
    # Label for "Range"
    range_label = tk.Label(dialog, text="Range:")
    range_label.pack()
    
    
    # Radio Buttons
    radio1 = tk.Radiobutton(dialog, text="0 to 1", variable=selected_type, value=0)
    radio2 = tk.Radiobutton(dialog, text="-1 to 1", variable=selected_type, value=1)
    
    radio1.pack()
    radio2.pack()
    
    
    # Button Frame for Show and Compare Buttons
    button_frame = tk.Frame(dialog)
    button_frame.pack()
    

    show_button = tk.Button(button_frame, text="Show", command=show)
    show_button.grid(row=0, column=0, padx=5)

    compare_button = tk.Button(button_frame, text="Compare", command=compare)
    compare_button.grid(row=0, column=1, padx=5)

    dialog.wait_window()