#ChordsApp
#A program that helps you write chord progressions and modulations

class circleOfFifths():
    def __init__(self):
        self.notes = ['C',('C#','Db'),'D',('D#','Eb'),('E','Fb'),'F',('F#','Gb'),'G',('G#','Ab'),'A',('A#','Bb'),('B','Cb')]
        self.keyNames = {'C' : 0 ,'G' : 7,'D' : 2 ,'A' : 9,'E' : 4,'B' : 11,'Gb' : 6, 'F#' : 6,'Db' : 1,'C#' : 1,'Ab': 8,'Eb' : 3,'Bb' : 10,'F' : 4}
        self.majorIntervals = [2,2,1,2,2,2]
        self.minorIntervals = [1,2,2,1,2,2]
        self.keys = {}


    def initialise(self):
        #Builds the key
        pass
     

    def buildKeys(self, keyName):
        #Create key object
        newKey = keys(keyName)
        root = self.keyNames[keyName]
        interval = root

        #If key is major
        for i in range(6):
            interval += self.majorIntervals[i]
            if interval >= 12:
                interval = interval - 12
            #Chooses the enharmonic relevant to the key
            if type(self.notes[interval]) == tuple:
                if 'b' in keyName or keyName == 'F':
                    newKey.scale.append(self.notes[interval][1])
                else:
                    newKey.scale.append(self.notes[interval][0])
            else:
                newKey.scale.append(self.notes[interval])

            
        return newKey


class keys():
    def __init__(self, keyName):
        self.keyName = keyName
        self.chords = {}
        self.scale = [keyName]

    def getScale(self):
        return self.scale

        


            

