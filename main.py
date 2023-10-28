
import tkinter as tk
from utils.new_wave_dialog import newWaveDialog
from utils import wave_drawer
from utils.signal_reader import readInputFromFile
from dialogs.arith_ops_dialog import showArithOpsDialog
from dialogs.quantization_dialog import openQuantizaDialog

window = tk.Tk() 
window.title('DSP')
window.geometry("960x540")

def showWave():
    example = readInputFromFile()[1]
    wave_drawer.draw(example)

def newWave():
    wave = newWaveDialog(window)
    wave_drawer.draw_wave(wave)

def arithmetic():
    showArithOpsDialog(window)

def quantize():
    openQuantizaDialog(window)

tk.Label(window, text="").pack()

openFileBtn = tk.Button(window, pady=4, text='Open File', width=25, command=showWave) 
openFileBtn.pack() 

newBtn = tk.Button(window, pady=4, text='New Wave', width=25, command=newWave) 
newBtn.pack()

arithBtn = tk.Button(window, pady=4, text='Arithmetic Ops', width=25, command=arithmetic) 
arithBtn.pack()

quantizeBtn = tk.Button(window, pady=4, text='Quantize Signal', width=25, command=quantize) 
quantizeBtn.pack()

window.mainloop() 