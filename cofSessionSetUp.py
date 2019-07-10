#cof getKey() test

import Chords2

#cof getKey() test

import Chords2

session = Chords2.session()
session.sessionSetUp()

aChords = session.circleOfFifths.keySignitures['A'].getChords()

print(aChords)