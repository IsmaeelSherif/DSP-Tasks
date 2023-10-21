import numpy as np

def addWave(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    if(len(arr1) > len(arr2)):
        arr2.resize(arr1.shape)
    elif(len(arr2) > len(arr1)):
        arr1.resize(arr2.shape)

    addResult = arr1 + arr2
    return addResult

def subWave(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    if(len(arr1) > len(arr2)):
        arr2.resize(arr1.shape)
    elif(len(arr2) > len(arr1)):
        arr1.resize(arr2.shape)

    subResult = arr1 - arr2
    return subResult

def multiplyWave(inputWave, factor):
    arr = np.array(inputWave)
    result = [element * factor for element in arr]
    return result

def squarWave(inputWave):
    arr = np.array(inputWave)
    result = [pow(element,2) for element in arr]
    return result

def shiftWave(inputWave, value):
    arr = np.array(inputWave)
    shifted = arr - value
    return shifted

def normalizeWave(inputWave, choice):
    arr = np.array(inputWave)
    if choice == 0 : # from 0 to 1
        normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
    elif choice == 1 : #from -1 to 1
        normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr)) * 2 - 1
    else:
        raise ValueError("Invalid choice.")

    return normalized

def accumulateWave(inputWave):
    arr = np.array(inputWave)
    accumulated = np.cumsum(arr)
    return accumulated