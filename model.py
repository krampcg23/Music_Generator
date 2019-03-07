from helper import drange, readMusic
from Sound import Note, Sound
from collections import defaultdict
import random
import os

class MarkovModel:
    def __init__ (self, n):
        self.model = defaultdict(Note)
        self.chainLength = n
        self.lengthOfSong = 100

    def readMusic_Model(self):
        l = os.listdir("music")
        for f in l:
            direc = "music/" + f
            self.addSong(direc)

    def addSong(self, f):
        sounds = readMusic(f)
        for i in drange(0, len(sounds)-1, 1):
            self.model.setdefault(sounds[i].getNote(), []).append(sounds[i+1])

    def generateMusic(self, seed):
        listOfSounds = self.model[seed]
        r = random.randint(0, len(listOfSounds)-1)
        sound = listOfSounds[r]
        for i in range(self.lengthOfSong):
            sound.playSound()
            if sound.getNote() not in self.model:
                sound = Sound(Note.DS, 4, 0.5)
            listOfSounds = self.model[sound.getNote()]
            r = random.randint(0, len(listOfSounds)-1)
            sound = listOfSounds[r]



