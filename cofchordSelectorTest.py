#cof getKey() test

import Chords2

#cof getKey() test

import Chords2

session = Chords2.session()
session.sessionSetUp()

usr = Chords2.chordSelector()

usr.selectKey(session.circleOfFifths, 'C')


#General tests
print(usr.currentKey.getChordSymbols())
print(usr.currentKey.keyName)
print(usr.currentKey.relativeMinor)


#Select chord test

currentKey = usr.currentKey.getChordSymbols()
usr.selectChord(currentKey[5])
print(usr.selectedChord)


