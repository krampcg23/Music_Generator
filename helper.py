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

durationToLily = { 2 : 4,
                 1.5 : 2,
                 1 : 1,
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
