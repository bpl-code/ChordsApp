#circleOfFifths.buildKeys() test

import chords

cof = chords.circleOfFifths()


C = cof.buildKeys('C')

print(C.scale)

G = cof.buildKeys('G')

print(G.scale)

D = cof.buildKeys('D')

print(D.scale)

Ab = cof.buildKeys('Ab')

print(Ab.scale)


CSharp = cof.buildKeys('c#')

print(Ab.scale)

B = cof.buildKeys('B')

print(B.scale)

Ab = cof.buildKeys('Ab')

print(Ab.scale)


{'C' : 0 ,'G' : 7,'D' : 2 ,'A' : 9,'E' : 4,'B' : 11,'Gb' : 6, 'F#' : 6,'Db' : 1,'C#' : 1,'Ab': 8,'Eb' : 3,'Bb' : 10,'F' : 4}