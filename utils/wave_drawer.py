
from models.wave import Wave
import matplotlib.pyplot as plt
import numpy as np

def draw(x, amplitudes):
  if(len(amplitudes) == 0):
    return
  
  plt.figure(1)
  plt.subplot(2, 1, 1)
  plt.plot(x, amplitudes)
  plt.title('Continuous Wave')
  plt.xlabel('Time')
  plt.ylabel('Amplitude')

  plt.figure(2)
  plt.subplot(2, 1, 1)
  plt.stem(x, amplitudes, linefmt='b--', markerfmt='bo', basefmt='k-')
  plt.title('Discrete Wave')
  plt.xlabel('Time')
  plt.ylabel('Amplitude')
  plt.show()


def draw_wave(wave):
  sampling_freq = wave.Fs
  analog_freq = wave.analogFreq
  amplitude = wave.amplitude
  phase_shift = wave.phaseShift
  # Calculate the time values
  t = np.arange(0, 1, 1/sampling_freq)
  # Calculate the angular frequency
  omega = 2 * np.pi * analog_freq
  waveArr = None

  if wave.isSine :
    sin_wave = amplitude * np.sin((omega * t ) + phase_shift)
    waveArr = sin_wave
  else: 
    cos_wave = amplitude * np.cos((omega * t ) + phase_shift )
    waveArr = cos_wave
    
    

  waveName = 'Cosine'
  if wave.isSine:
    waveName = 'Sine'
  
  plt.figure(1)
  plt.subplot(2, 1, 1)
  plt.plot(t, waveArr)
  plt.title('Continuous ' + waveName + " Wave")
  plt.xlabel('Time')
  plt.ylabel('Amplitude')

  plt.figure(2)
  plt.subplot(2, 1, 1)
  plt.stem(t, waveArr, linefmt='b--', markerfmt='bo', basefmt='k-')
  plt.title('Discrete ' + waveName + ' Wave')
  plt.xlabel('Time')
  plt.ylabel('Amplitude')
  plt.show()
  
  
