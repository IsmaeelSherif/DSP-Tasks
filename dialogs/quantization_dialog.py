import tkinter as tk
from utils import wave_drawer
from utils.signal_reader import readInputFromFile
from testwave.Task3.Test1.QuanTest1 import QuantizationTest1
from testwave.Task3.Test2.QuanTest2 import QuantizationTest2
import numpy as np
import math as mt

def show_output(arr1,arr2,arr3,arr4):
    i=0
    for i in range(len(arr1)) :
        print(arr1[i],arr2[i],arr3[i],arr4[i])

def show_output2(arr1,arr2):
    i=0
    for i in range(len(arr1)) :
        print(arr1[i],arr2[i])

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
            number_of_bits = int(mt.log2(noOfBitsOrLevels))
            arr = np.array(magnitudes)
            maximum = max(arr)
            minimum = min(arr)
            delta = (maximum - minimum) / number_of_levels
            ranges = np.arange(start=minimum, stop=maximum, step=delta)
            ranges = [round(element , 2) for element in ranges]
            quantized = []
            midpoints = []
            x = round(minimum,2)
            while x < maximum:
                midpoint = (x+(x + delta))/2
                midpoint = round(midpoint, 3)
                midpoints.append(midpoint)
                print("midpoint for : ",x,"and ",x+delta,"is : ",midpoint)
                x = round( x + delta , 2)

            distances = []
            error = []
            which_interval = []
            which_interval_encoded = []


            for i in range(len(arr)):
                item = arr[i]
                distances = [element - item  for element in midpoints]
                min_dis = min(distances, key=abs)
                error.append(round(min_dis, 3))
                level = distances.index(min_dis)+1
                quantized.append( midpoints[level-1])
                which_interval.append(level)
                which_interval_encoded.append(convert_to_binary(level-1 , number_of_bits))
            print(len(which_interval) , len(which_interval_encoded) , len(quantized) , len(error))
            show_output(which_interval , which_interval_encoded , quantized ,error)
            return which_interval,which_interval_encoded,quantized,error

        else:  # bits
            number_of_levels = mt.pow(2 , noOfBitsOrLevels)
            number_of_bits = noOfBitsOrLevels
            arr = np.array(magnitudes)
            maximum = max(arr)
            minimum = min(arr)
            delta = (maximum - minimum) / number_of_levels
            ranges = np.arange(start=minimum, stop=maximum, step=delta)
            ranges = [round(element, 2) for element in ranges]
            quantized = []
            midpoints = []
            x = round(minimum, 2)
            while x < maximum:
                midpoint = (x + (x + delta)) / 2
                midpoint = round(midpoint, 3)
                midpoints.append(midpoint)
                print("midpoint for : ", x, "and ", x + delta, "is : ", midpoint)
                x = round(x + delta, 2)

            distances = []
            error = []
            which_interval = []
            which_interval_encoded = []

            for i in range(len(arr)):
                item = arr[i]
                distances = [element - item for element in midpoints]
                min_dis = min(distances, key=abs)
                error.append(round(min_dis, 3))
                level = distances.index(min_dis) + 1
                quantized.append(midpoints[level - 1])
                which_interval.append(level)
                which_interval_encoded.append(convert_to_binary(level - 1, number_of_bits))
            show_output2(which_interval_encoded, quantized)

            return which_interval_encoded, quantized


    def testResult(result):
        import os
        import sys

        rootPath = os.path.dirname(sys.argv[0])
        if('1' in inputSignal.fileName):
            filename = rootPath + '/testwave/Task3/Test1/Quan1_input.txt'
            QuantizationTest1(filename, result[0], result[1])
        elif('2' in inputSignal.fileName):
            filename = rootPath + '/testwave/Task3/Test2/Quan2_input.txt'
            QuantizationTest2(filename, result[0], result[1], result[2], result[3])

    def show():
        if(inputSignal):
            result = calculateQuantizedSignal()
            if(result):
                testResult(result)
                wave_drawer.draw(inputSignal.x, result)

    
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