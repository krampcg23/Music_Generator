from Sound import Note, Sound
from helper import getNote, readMusic, playMusic

if __name__ == '__main__' :
    sounds = readMusic("FurElise.txt")
    playMusic(sounds)

