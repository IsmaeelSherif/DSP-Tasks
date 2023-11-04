

class Signal:
  def __init__(self, x, y, name):
    self.fileName = name
    self.x = x
    self.magnitudes = y


class FDSignal:
  def __init__(self, amplitudes, phaseShifts, name):
    self.fileName = name
    self.amplitudes = amplitudes
    self.phaseShifts = phaseShifts