#circleOfFifths.buildKeys() test

import chords

cof = chords.circleOfFifths()

cMajor = cof.buildKeys('B')

print(cMajor.scale)

Ab = cof.buildKeys('Ab')

print(Ab.scale)
