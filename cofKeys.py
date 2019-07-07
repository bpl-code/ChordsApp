#circleOfFifths.buildKeys() test

import Chords2

cof = Chords2.circleOfFifths()

cof.buildKeys()

key = cof.keySignitures['A']

print(key.getChords())
