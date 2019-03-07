from Sound import Note, Sound

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
        l = line.split()
        for i in drange(0, len(l), 3):
            s = Sound(getNote(l[i]), float(l[i+1]), float(l[i+2]))
            sounds.append(s)

    return sounds

def playMusic(sounds):
    for s in sounds:
        s.playSound()
