#ChordsApp
#A program that helps you write chord progressions and modulations

class circleOfFifths():
    def __init__(self):
        self.notes = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']
        self.keyNames = ['c','g','d','a','e','b','gb','db','ab','eb','bb','f']
        self.majorIntervals = [2,2,1,2,2,2,1]


    def initialise(self):
        pass
     

    def buildKeys(self, key):
        #Create key object
        newKey = keys(key)
        interval = self.notes.index(key)
        for i in range(7):
            interval += self.majorIntervals[i]
            if interval >= 12:
                interval = interval - 12
            newKey.scale.append(self.notes[interval])
        return newKey


class keys():
    def __init__(self, keyName):
        self.keyName = keyName
        self.chords = {}
        self.scale = [keyName]

