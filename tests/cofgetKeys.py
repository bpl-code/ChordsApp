#cof getKey() test

import Chords2

cof = Chords2.circleOfFifths()

cof.buildKeys()

for key in list(cof.keyScales.keys()):
    print(cof.getKey(key).getChords())