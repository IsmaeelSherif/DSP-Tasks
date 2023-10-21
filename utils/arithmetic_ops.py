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