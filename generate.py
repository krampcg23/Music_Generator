import random
f = open("randomMusic.txt", 'w')
notes = ['C', 'CS', 'D', 'DS', 'E', 'F', 'FS', 'G', 'GS', 'A', 'AS', 'B']
for i in range(200):
    r = random.randint(0, len(notes)-1)
    d = random.uniform(0.1, 2)
    line = notes[r] + " " + str(round(d, 1))
    f.write(line)
    f.write('\n')

f.close()
