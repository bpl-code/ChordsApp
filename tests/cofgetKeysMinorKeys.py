#cof getKey() test

import Chords2

cof = Chords2.circleOfFifths()

cof.buildKeys()

print(len(cof.keySignitures))

for key in cof.keySignitures:
    print(key + ' ' + str(cof.keySignitures[key].getChords()))

