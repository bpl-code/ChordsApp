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

usr.pivotMod()

for key,val in usr.pivotModKeys.items():
    print("Key = {}  Chords = {}".format(key,val.chordSymbols))

for key,val in usr.pivotModKeys.items():
    print("Key = {}  Chords = {}".format(key,val.chordNames))

