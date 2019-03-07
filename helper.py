from Sound import Note, Sound
import random

noteDict = {'C'  : Note.C,
            'CS' : Note.CS,
            'D'  : Note.D,
            'DS' : Note.DS,
            'E'  : Note.E,
            'F'  : Note.F,
            'FS' : Note.FS,
            'G'  : Note.G,
            'GS' : Note.GS,
            'A'  : Note.A,
            'AS' : Note.AS,
            'B'  : Note.B }

noteToLily = { Note.C  : 'c',
               Note.CS : 'cis',
               Note.D  : 'd',
               Note.DS : 'dis',
               Note.E  : 'e',
               Note.F  : 'f',
               Note.FS : 'fis',
               Note.G  : 'g',
               Note.GS : 'gis',
               Note.A  : 'a',
               Note.AS : 'as',
               Note.B  : 'b' }

durationToLily = { 2 : 2,
                 1.5 : 2,
                 1 : 4,
                 0.5 : 8}

def durationLily(duration):
    return durationToLily[duration]

def getLily(note):
    return noteToLily[note]

def getNote(note):
    return noteDict[note]

def drange(start, stop, step):
    while start < stop:
            yield start
            start += step

def readMusic(f):
    F = open(f, 'r')
    sounds = []
    for line in F:
        if (line[0] == "#"):
            continue
        l = line.split()
        for i in drange(0, len(l), 3):
            s = Sound(getNote(l[i]), float(l[i+1]), float(l[i+2]))
            sounds.append(s)

    return sounds

def playMusic(sounds):
    for s in sounds:
        s.playSound()

def generate():
    f = open("randomMusic.txt", 'w')
    notes = ['C', 'CS', 'D', 'DS', 'E', 'F', 'FS', 'G', 'GS', 'A', 'AS', 'B']
    for i in range(200):
        r = random.randint(0, len(notes)-1)
        d = random.uniform(0.1, 2)
        line = notes[r] + " " + str(round(d, 1))
        f.write(line)
        f.write('\n')

    f.close()
