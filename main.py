from Sound import Note, Sound
from helper import getNote, readMusic, playMusic
from model import MarkovModel

if __name__ == '__main__' :
    #sound = Sound(Note.E, 10)
    #sound.playSound()
    #sound2 = Sound(Note.G, 10)
    #sound.playChord(sound2)

    mm = MarkovModel(1)
    mm.readMusic_Model()
    mm.generateMusic(Note.DS)
    #sounds = readMusic("music/summers.txt")
    #sounds = readMusic("music/canon.txt")
    #playMusic(sounds)

