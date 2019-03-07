from Sound import Note, Sound
from helper import getNote, readMusic, playMusic
from model import MarkovModel

if __name__ == '__main__' :
    #sound = Sound(Note.E, 10)
    #sound.playSound()
    #seed = Sound(Note.A, 5, 1)

    mm = MarkovModel(2)
    mm.readMusic_Model()
    seed = (Note.A, Note.B)
    #seed = Note.A
    mm.generateMusic(seed)
    #sounds = readMusic("music/summers.txt")
    #sounds = readMusic("music/canon.txt")
    #playMusic(sounds)

