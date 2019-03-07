from helper import drange, readMusic, getLily, durationLily
from Sound import Note, Sound
from collections import defaultdict
import random
import os

class MarkovModel:
    def __init__ (self, n):
        if n == 1:
            self.model = defaultdict(Note)
        else:
            self.model = defaultdict((Note))
        self.chainLength = n
        self.lengthOfSong = 50

    def saveMusic(self, music):
        f = open("newSong.ly", "w")
        f.write("\header { \n")
        f.write('title = "My Lovely Song"\n')
        f.write('}\n')
        f.write("{\n")
        f.write("\\time 4/4\n")
        counter = 0
        prevDuration = '0'
        for sound in music:
            note = getLily(sound.note)
            if sound.octave > 4:
                for i in range(int(sound.octave) - 4):
                    note = note + "'"
            elif sound.octave < 4:
                for i in range(4 - int(sound.octave)):
                    note = note = ","
            myDuration = str(durationLily(sound.duration))
            if prevDuration != myDuration:
                note = note + myDuration
            prevDuration = myDuration
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
        for i in drange(0, len(sounds)-self.chainLength, 1):
            if self.chainLength == 1:
                self.model.setdefault(sounds[i].getNote(), []).append(sounds[i+1])
            else:
                chain = []
                for j in range(self.chainLength):
                    chain.append(sounds[i+j].getNote())
                chainTuple = tuple(chain)
                self.model.setdefault(chainTuple, []).append(sounds[i+self.chainLength])

    def generateMusic(self, seed):
        listOfSounds = self.model[seed]
        r = random.randint(0, len(listOfSounds)-1)
        sound = listOfSounds[r]
        theSong = []
        if self.chainLength != 1:
            newSeed = seed[1:self.chainLength] + (sound.getNote(),)
        for i in range(self.lengthOfSong):
            theSong.append(sound)
            sound.playSound()
            if self.chainLength == 1:
                if sound.getNote() not in self.model:
                    sound = seed
            else:
                if newSeed not in self.model:
                    sound = seed
                    newSeed = seed
                else:
                    sound = newSeed
            listOfSounds = self.model[sound]
            r = random.randint(0, len(listOfSounds)-1)
            sound = listOfSounds[r]
            newSeed = newSeed[1:self.chainLength] + (sound.getNote(),)

        self.saveMusic(theSong)




