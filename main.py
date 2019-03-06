from Sound import Note, Sound
from helper import getNote, readMusic, playMusic
from model import MarkovModel

if __name__ == '__main__' :
    mm = MarkovModel(1)
    mm.readMusic()
    mm.generateMusic(Note.DS)
    #sounds = readMusic("FurElise.txt")
    #sounds = readMusic("music/canon.txt")
    #playMusic(sounds)

