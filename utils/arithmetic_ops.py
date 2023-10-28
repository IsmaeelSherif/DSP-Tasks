import numpy as np
from models.signal import Signal

def addWave(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    if(len(arr1) > len(arr2)):
        arr2.resize(arr1.shape)
    elif(len(arr2) > len(arr1)):
        arr1.resize(arr2.shape)

    addResult = arr1 + arr2
    return addResult

def subWave(signal1, signal2):
    arr1 = np.array(signal1.magnitudes)
    arr2 = np.array(signal2.magnitudes)
    if(len(arr1) > len(arr2)):
        arr2.resize(arr1.shape)
    elif(len(arr2) > len(arr1)):
        arr1.resize(arr2.shape)

    subResult = arr1 - arr2
    return subResult

def multiplyWave(inputWave, factor):
    arr = np.array(inputWave.magnitudes)
    result = [element * factor for element in arr]
    return result

def squarWave(inputWave):
    arr = np.array(inputWave.magnitudes)
    result = [pow(element,2) for element in arr]
    return result

def shiftWave(signal, value):
    arr = np.array(signal.x)
    resultX = [element - value for element in arr]
    return Signal(resultX, signal.magnitudes, signal.fileName)

def normalizeWave(inputWave, choice):
    arr = np.array(inputWave.magnitudes)
    if choice == 0 : # from 0 to 1
        normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
    elif choice == 1 : #from -1 to 1
        normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr)) * 2 - 1
    else:
        raise ValueError("Invalid choice.")

    return normalized

def accumulateWave(inputWave):
    arr = np.array(inputWave.magnitudes)
    accumulated = np.cumsum(arr)
    return accumulated.tolist()