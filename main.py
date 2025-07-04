
import tkinter as tk
from utils import wave_drawer
from utils.signal_reader import readInputFromFile
from dialogs.new_wave_dialog import newWaveDialog
from dialogs.arith_ops_dialog import showArithOpsDialog
from dialogs.quantization_dialog import openQuantizaDialog
from dialogs.freq_domain_dialog import openFreqDomainDialog
from dialogs.time_domain_dialog import openTimeDomainDialog
from dialogs.convolution_dialog import openConvDialog
from dialogs.correlation_dialog import openCorrelationDialog
from dialogs.fast_convolution_dialog import openFastConvDialog
from dialogs.fast_correlation_dialog import openFastCorrelationDialog
window = tk.Tk() 
window.title('DSP')
window.geometry("960x540")

def showWave():
    example = readInputFromFile()
    wave_drawer.draw(example.x, example.magnitudes)

def newWave():
    wave = newWaveDialog(window)
    wave_drawer.draw_wave(wave)

def arithmetic():
    showArithOpsDialog(window)

def quantize():
    openQuantizaDialog(window)

def freqDom():
    openFreqDomainDialog(window)

def timeDom():
    openTimeDomainDialog(window)

def conv():
    openConvDialog(window)

def corr():
    openCorrelationDialog(window)

def fastConv():
    openFastConvDialog(window)

def fastCorr():
    openFastCorrelationDialog(window)

tk.Label(window, text="").pack()

openFileBtn = tk.Button(window, pady=4, text='Open File', width=25, command=showWave) 
openFileBtn.pack() 

newBtn = tk.Button(window, pady=4, text='New Wave', width=25, command=newWave) 
newBtn.pack()

arithBtn = tk.Button(window, pady=4, text='Arithmetic Ops', width=25, command=arithmetic) 
arithBtn.pack()

quantizeBtn = tk.Button(window, pady=4, text='Quantize Signal', width=25, command=quantize) 
quantizeBtn.pack()

freqDomainBtn = tk.Button(window, pady=4, text='Frequency Domain', width=25, command=freqDom) 
freqDomainBtn.pack()

timeDomainBtn = tk.Button(window, pady=4, text='Time Domain', width=25, command=timeDom) 
timeDomainBtn.pack()

convBtn = tk.Button(window, pady=4, text='Convolution', width=25, command=conv) 
convBtn.pack()

corrBtn = tk.Button(window, pady=4, text='Correlation', width=25, command=corr)
corrBtn.pack()

fastConvBtn = tk.Button(window, pady=4, text='Fast Convolution', width=25, command=fastConv) 
fastConvBtn.pack()

fastCorrelationBtn = tk.Button(window, pady=4, text='Fast Correlation', width=25, command=fastCorr)  # Add this line
fastCorrelationBtn.pack()

window.mainloop() 