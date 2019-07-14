#cof getKey() test

import chords

session = chords.session()
session.sessionSetUp()

usr = chords.chordSelector(session)

usr.selectKey('C')

print(usr.currentKey.chordSymbols)
print(usr.currentKey.chordNames)

usr.selectChord('GM')

print(usr.selectedChord)

usr.parallelMod()

print(usr.parallelKey.keyName)
