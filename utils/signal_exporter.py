from models.signal import Signal, FDSignal


def exportSignalToFile(signal, relativePath):
    
    array1 = None
    array2 = None
    periodic = None

    if isinstance(signal, Signal):
        array1 = signal.x
        array2 = signal.magnitudes
        periodic = 0
    elif isinstance(signal, FDSignal):
        array1 = signal.amplitudes
        array2 = signal.phaseShifts
        periodic = 1
    
    N = len(array1)

    if len(array1) == len(array2):
        with open(relativePath, 'w') as file:
            file.write("0\n")
            file.write(f"{periodic}\n")
            file.write(f"{N}\n")
            for i in range(len(array1)):
                line = f"{array1[i]} {array2[i]}\n"
                file.write(line)


    print('Successfully exported')