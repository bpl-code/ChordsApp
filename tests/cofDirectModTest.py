#cof getKey() test

import Chords2

#cof getKey() test

import Chords2

session = Chords2.session()
session.sessionSetUp()

usr = Chords2.chordSelector(session)

usr.selectKey('C')

print(usr.currentKey.chordSymbols)
print(usr.currentKey.chordNames)

usr.selectChord('GM')

print(usr.selectedChord)

usr.directMod()

for key,val in usr.directModKeys.items():
    print("Key = {}  Chords = {}".format(key,val.chordNames))


