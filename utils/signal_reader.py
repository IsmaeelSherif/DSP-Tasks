
from tkinter.filedialog import askopenfilename
from models.signal import Signal
import os


def readInputFromFile():
  file_path = askopenfilename()
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
  is_periodic = bool(lines[1])
  #Parse N1 (Number of samples or frequencies)
  numberOfSamples = int(lines[2])
  if(isTimeBased):
    x = [0] * numberOfSamples
    y = [0] * numberOfSamples
    for i in range(0, numberOfSamples):
      parts = lines[i + 3].split()  # Split the line into parts using whitespace as the delimiter

      x[i] = int(parts[0])
      y[i] = float(parts[1])

    signal = Signal(x, y, displayFileName)
    return signal

    