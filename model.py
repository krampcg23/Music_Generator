from helper import drange, readMusic, getLily, durationLily
from Sound import Note, Sound
from collections import defaultdict
import random
import os

class MarkovModel:
    def __init__ (self, n):
        self.model = defaultdict(Note)
        self.chainLength = n
        self.lengthOfSong = 100

    def saveMusic(self, music):
        f = open("newSong.ly", "w")
        f.write("\header { \n")
        f.write('title = "My Lovely Song"\n')
        f.write('}\n')
        f.write("{\n")
        counter = 0
        for sound in music:
            note = getLily(sound.note)
            if sound.octave > 4:
                for i in range(int(sound.octave) - 4):
                    note = note + "'"
            elif sound.octave < 4:
                for i in range(4 - int(sound.octave)):
                    note = note = ","
            note = note + str(durationLily(sound.duration))
            f.write(note + " ")
            counter = counter + 1
            if (counter == 4):
                f.write("\n")
                counter = 0

        f.write("\n}\n")
        f.write('\\version "2.18.2" ')
        f.close()


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
        theSong = []
        for i in range(self.lengthOfSong):
            theSong.append(sound)
            sound.playSound()
            if sound.getNote() not in self.model:
                sound = Sound(Note.DS, 4, 0.5)
            listOfSounds = self.model[sound.getNote()]
            r = random.randint(0, len(listOfSounds)-1)
            sound = listOfSounds[r]
        self.saveMusic(theSong)




