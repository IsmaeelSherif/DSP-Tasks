

class Wave:
  def __init__(self, attributes = None, isSine = None, amplitude = None, analogF = None, fs = None, phaseShift = None):
    if(attributes != None):
        self.type = attributes['type']
        self.isSine = attributes['type'] == 'sin'
        self.amplitude = int(attributes['A'])
        self.analogFreq = int(attributes['AnalogFrequency'])
        self.Fs = int(attributes['SamplingFrequency'])
        self.phaseShift = float(attributes['PhaseShift'])
    else:
        self.isSine = isSine
        self.amplitude = amplitude
        self.analogFreq = analogF
        self.Fs = fs
        self.phaseShift = phaseShift
    