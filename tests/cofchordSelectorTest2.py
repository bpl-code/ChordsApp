#cof getKey() test

import Chords2

#cof getKey() test

import Chords2

session = Chords2.session()
session.sessionSetUp()

usr = Chords2.chordSelector()

usr.selectKey(session.circleOfFifths, 'C')

print(usr.currentKey.chordSymbols)
print(usr.currentKey.chordNames)

usr.selectChord('GM')

print(usr.selectedChord)


