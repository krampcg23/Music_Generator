from Sound import Note, Sound

def readMusic(f):


if __name__ == '__main__' :
    sounds = readMusic("FurElise.txt")
    S = Sound(Note.C, 4)
    S.playSound()
