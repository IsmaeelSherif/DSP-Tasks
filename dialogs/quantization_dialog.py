import tkinter as tk
from utils import wave_drawer
from utils.signal_reader import readInputFromFile
from testwave.Task3.Test1.QuanTest1 import QuantizationTest1
from testwave.Task3.Test2.QuanTest2 import QuantizationTest2
import numpy as np
import math as mt


def convert_to_binary(number, num_bits):
    binary = bin(number)[2:]  # Convert number to binary string
    binary = binary.zfill(num_bits)  # Pad the binary string with
    return binary

def openQuantizaDialog(root):

    inputSignal = None
    # Create a IntVar to store the selected type
    selected_type = tk.StringVar(value='levels')


    def change_label_text(label):
        nonlocal inputSignal
        inputSignal = readInputFromFile()
        if(inputSignal):
            label.config(text=inputSignal.fileName)

    def calculateQuantizedSignal():
        # selected_type can be either 'levels' or 'bits'
        magnitudes = inputSignal.magnitudes
        noOfBitsOrLevels = 0
        try:
            noOfBitsOrLevels = int(text_input.get())
        except:
            print('Put a correct integer value')
            return

        if selected_type.get() == 'levels':
            number_of_levels = noOfBitsOrLevels
            number_of_bits = int(mt.log2(number_of_levels))
            arr = np.array(magnitudes)
            maximum = max(arr)
            minimum = min(arr)
            delta = (maximum - minimum) / number_of_levels
            ranges = [minimum]
            for i in range(1, number_of_levels):
                newVal = ranges[i-1] + delta
                ranges.append(newVal)
            ranges.append(maximum)
            ranges = [round(element , 2) for element in ranges]
            
            quantized = []
            midpoints = []
            
            for i in range(0, len(ranges) - 1):
                midpoint = (ranges[i+1] + ranges[i]) / 2
                midpoints.append(midpoint)

            error = []
            which_interval = []
            which_interval_encoded = []


            for item in magnitudes:
                levelIndex = 0
                for i in range(0, len(ranges)):
                    if ranges[i] >= item:
                        if i > 0:
                            levelIndex = i - 1
                        else:
                            levelIndex = 0
                        break
                level = levelIndex + 1

                error.append( midpoints[levelIndex] - item )
                quantized.append( midpoints[levelIndex])
                which_interval.append(level)
                which_interval_encoded.append(convert_to_binary(levelIndex , number_of_bits))
            return which_interval,which_interval_encoded,quantized,error

        else:  # bits
            number_of_bits = noOfBitsOrLevels
            number_of_levels = int(mt.pow(2 , number_of_bits))
            
            arr = np.array(magnitudes)
            maximum = max(arr)
            minimum = min(arr)
            delta = (maximum - minimum) / number_of_levels
            ranges = [minimum]
            for i in range(1, number_of_levels):
                newVal = ranges[i-1] + delta
                ranges.append(newVal)
            ranges.append(maximum)
            ranges = [round(element , 2) for element in ranges]

            quantized = []
            midpoints = []
            
            for i in range(0, len(ranges) - 1):
                midpoint = (ranges[i+1] + ranges[i]) / 2
                midpoints.append(midpoint)

            error = []
            which_interval_encoded = []

            for item in magnitudes:

                levelIndex = 0
                for i in range(0, len(ranges)):
                    if ranges[i] >= item:
                        if i > 0:
                            levelIndex = i - 1
                        else:
                            levelIndex = 0
                        break
                level = levelIndex + 1

                error.append(item - midpoints[levelIndex])
                quantized.append( midpoints[levelIndex])
                which_interval_encoded.append(convert_to_binary(levelIndex , number_of_bits))


            return which_interval_encoded, quantized


    def testResult(result):
        import os
        import sys

        rootPath = os.path.dirname(sys.argv[0])
        
        if('1' in inputSignal.fileName):
            filename = rootPath + '/testwave/Task3/Test1/Quan1_Out.txt'
            QuantizationTest1(filename, result[0], result[1])
        elif('2' in inputSignal.fileName):
            filename = rootPath + '/testwave/Task3/Test2/Quan2_Out.txt'
            QuantizationTest2(filename, result[0], result[1], result[2], result[3])

    def show():
        if(inputSignal):
            result = calculateQuantizedSignal()
            if(result):
                testResult(result)
                quantizedIndex = 1 if selected_type.get() == 'bits' else 2
                wave_drawer.draw(inputSignal.x, result[quantizedIndex])

    
    dialog = tk.Toplevel(root)
    dialog.grab_set()
    dialog.title("Signal Quantization")
    dialog.geometry("360x300")




    # Create a frame for the components
    frame = tk.Frame(dialog, padx=10, pady=10)
    frame.pack()
    
    button1 = tk.Button(frame, text="Input Signal", command=lambda: change_label_text(label1))
    button1.grid(row=0, column=0, padx=5)
    label1 = tk.Label(frame, text="")
    label1.grid(row=0, column=1)
    
    # Radio Buttons
    level_radio = tk.Radiobutton(frame, text="Levels", variable=selected_type, value="levels")
    bit_radio = tk.Radiobutton(frame, text="Bits", variable=selected_type, value="bits")
    
    level_radio.grid(row=1, column=0, padx=5, pady=10, sticky=tk.W)
    bit_radio.grid(row=1, column=1, padx=5, pady=10, sticky=tk.W)
    
    # Text Input Field
    text_input = tk.Entry(frame)
    text_input.grid(row=2, column=0, columnspan=2, pady=10)
    
    # Button
    show_button = tk.Button(frame, text="Show", command=show)
    show_button.grid(row=3, column=0, columnspan=2, pady=10)

    dialog.wait_window()