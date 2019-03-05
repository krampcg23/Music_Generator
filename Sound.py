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


fs = 44100 # The Sample Rate
class Sound:
    noteToHz = {Note.C  : 261.63,
                Note.CS : 277.18,
                Note.D  : 293.66,
                Note.DS : 311.13,
                Note.E  : 329.63,
                Note.F  : 349.23,
                Note.FS : 369.99,
                Note.G  : 392.00,
                Note.GS : 415.30,
                Note.A  : 440.00,
                Note.AS : 466.16,
                Note.B  : 493.88 }

    def __init__(self):
        self.note = Note.C
        self.duration = 0
        self.volume = 0.5

    def __init__(self, note, duration):
        self.note = note
        self.duration = duration
        self.volume = 0.5

    def getHz(self):
        return Sound.noteToHz[self.note]

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
