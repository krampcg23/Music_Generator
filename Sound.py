from enum import Enum
import numpy as np
import scipy.signal
import pyaudio

class Note(Enum):
    C = 1
    CS = 2
    D = 3
    DS = 4
    E = 5
    F = 6
    FS = 7
    G = 8
    GS = 9
    A = 10
    AS = 11
    B = 12

fs = 44100
class Sound:
    noteToHz = {Note.C  : 16.351,
                Note.CS : 17.324,
                Note.D  : 18.354,
                Note.DS : 19.445,
                Note.E  : 20.601,
                Note.F  : 21.827,
                Note.FS : 23.124,
                Note.G  : 24.499,
                Note.GS : 25.956,
                Note.A  : 27.5,
                Note.AS : 29.135,
                Note.B  : 30.868}

    def __init__(self):
        self.note = Note.C
        self.duration = 0
        self.volume = 0.5
        self.octave = 4

    def __init__(self, note, octave, duration):
        self.note = note
        self.octave = octave
        self.duration = duration
        self.volume = 0.5

    def __eq__(self, other):
        if (self.note == other.note):
            return seld.duration == other.duration
        else: return self.note == other.note

    def getNote(self):
        return self.note

    def getHz(self):
        return Sound.noteToHz[self.note] * pow(2, self.octave)

    def generateWave(self):
        return (np.sin(2*np.pi*np.arange(fs*self.duration)*self.getHz()/fs)).astype(np.float32)

    def playSound(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
        samples = self.generateWave()
        stream.write(self.volume*samples)
        stream.stop_stream()
        stream.close()
        p.terminate()
