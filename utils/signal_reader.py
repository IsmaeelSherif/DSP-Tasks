
from tkinter.filedialog import askopenfilename
from models.signal import Signal, FDSignal
import os


def readInputFromFile(defaultPath = ""):
  file_path = askopenfilename(initialdir=defaultPath)
  displayFileName = ""

  if file_path:
     # Get the last subfolder and file name
     last_subfolder = os.path.basename(os.path.dirname(file_path))
     file_name = os.path.basename(file_path)
     displayFileName = os.path.join(last_subfolder, file_name)
  else:
     return None
  
  with open(file_path, 'r') as file:
        lines = file.readlines()
   # Parse SignalType (0 for Time, 1 for Freq)
  isTimeBased = int(lines[0]) == 0
  #Parse IsPeriodic (0 or 1)
  is_periodic = bool(int(lines[1].strip()) == 1)
  #Parse N1 (Number of samples or frequencies)
  numberOfSamples = int(lines[2])
  if(isTimeBased):
    x = [0] * numberOfSamples
    y = [0] * numberOfSamples
    for i in range(0, numberOfSamples):
      parts = lines[i + 3].split()  # Split the line into parts using whitespace as the delimiter

      xAsString = parts[0].replace('f', '')
      yAsString = parts[1].replace('f', '')
      
      x[i] = float(xAsString)
      y[i] = float(yAsString)

    if is_periodic:
       signal = FDSignal(x, y, displayFileName)
    else:  
      signal = Signal(x, y, displayFileName)
    return signal

    