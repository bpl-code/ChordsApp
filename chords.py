#Chords Alt Version
# -*- coding: utf-8 -*-
#A program that helps you write chord progressions and modulations

class session():
    def __init__(self):
        self.circleOfFifths = ""

    def sessionSetUp(self):
        self.circleOfFifths = circleOfFifths()
        self.circleOfFifths.buildKeys()
        

class circleOfFifths():
    def __init__(self):
        self.keyNames = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B']
        self.keyScales = {'C' : ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'C#' : ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#'],\
        'Db' : ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'], 'D' : ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],\
        'D#' : ['D#', 'E#', 'F##', 'G#', 'A#', 'B#', 'C##'],\
        'Eb' : ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'], 'E' : ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],\
        'F' : ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'], 'F#' : ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#'],\
        'Gb' : ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F', 'Gb'], 'G' : ['G', 'A','B', 'C', 'D', 'E', 'F#'],\
        'G#' : ['G#', 'A#', 'B#', 'C#', 'D#', 'E#', 'F##'], 'Ab' : ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],\
        'A' : ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'A#' : ['A#', 'B#', 'C##', 'D#', 'E#', 'F##', 'G##'],\
        'Bb' : ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'], 'B' : ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']}
        self.keySignitures = {}

    def buildKeys(self):
        #Create key object
        for key in self.keyNames:
            self.keySignitures[key] = keys(key, self.keyScales[key])

        #Build Minor Keys
        for key in self.keyNames: 
            scale = self.keyScales[key]
            minorScale = [] 
            minorKeyName = scale[5] + 'm'
            for i in range(7):
                interval = 5 + i
                if interval > 6:
                    interval -= 7
                minorScale.append(scale[interval])
            self.keySignitures[minorKeyName] = keys(minorKeyName, minorScale, chordSymbols=['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII'])

    def getKey(self, keyName):
        return self.keySignitures[keyName]



class keys():
    def __init__(self, keyName, scale, chordSymbols=['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']):
        self.keyName = keyName
        self.scale = scale
        self.keySymbols = chordSymbols
        self.relativeMinor = scale[5] + 'm'
        self.relativeMajor = scale[1]
        self.chordSymbols = self.setChordSymbols()
        self.chordNames = self.setChordNames()

    #Functions
    def setChordSymbols(self):
        chords = []
        for i in range(7):
            chords.append(self.scale[i] + self.keySymbols[i])
        return chords

    def setChordNames(self):
        chordSymbols = self.getChordSymbols()
        chords = []
        for chord in chordSymbols:
            if '°' in chord:
                chords.append(chord[0] + 'dim')
            elif chord[1] == '#':
                if chord[2].islower():
                    chords.append(chord[0] + '#m')
                else:
                    chords.append(chord[0]+'#M')
            elif chord[1].islower():
                chords.append(chord[0] + 'm')
            else:
                chords.append(chord[0]+'M')
        return chords


    #Get Functions

    def getScale(self):
        return self.scale

    def getChordSymbols(self):
        return self.chordSymbols

    def getChords(self):
        return self.chordNames



    

class chordSelector():
    def __init__(self, session):
        self.session = session
        self.currentKey = None
        self.selectedChord = None
        self.previousKeys = []
        self.pivotModKeys = None

    #usr select functions
    
    def selectKey(self,key):
        self.manageKeyMemory()
        self.currentKey = self.session.circleOfFifths.keySignitures[key]
        self.selectedChord = None
        self.pivotModKeys = None

    def selectChord(self,chordName):
        self.selectedChord = chordName
 
    #functions

    def manageKeyMemory(self):
        if self.previousKeys == 5:
            tempList = []
            for i in range(1,6):
                tempList.append(self.previousKeys[i])
                tempList.append(self.currentKey)
                self.previousKeys = tempList
            else:
                self.previousKeys.append(self.currentKey)

    def pivotMod(self):
        self.pivotModKeys = {}
        for key,val in self.session.circleOfFifths.keySignitures.items():
            chords = val.chordNames
            if self.selectedChord in chords:
        self.pivotModKeys[key] = val
        self.pivotModKeys self.pivotModKeys  

    def parallelMod(self):
        # Parrallel keys are major scales and a minor scales that have the same tonic
        pass

    def truckDriverMod(self):
        #show the dominent chord of the key that is a step above the current key
        pass

    def alteredCommonMod(self):
        #This is when two keys share the same root note of a chord, but the quality is different.
        pass
    def setUpMod(self):
        #Step up either a half step or full step
        pass

    #get functions

    def getCurrentKey(self):
        return self.currentKey

    def getSelectedChord(self):
        return self.selectedChord

    def getpivotModKeys(self):
        return self.pivotModKeys

#DIRECT MOD

#Select chords DONE

#List keys that this chord belongs DONE

#Show new key relation so its roman numeral

#switch to new key

#store previous key


#Modulations to add

#Step-up mod - up half a step or a step (add both options?)
#truck driver - show the dominent chord of the key that is a step above the current key
#Altered Common chord mod - This is when two keys share the same root note of a chord, but the quality is different.
#Pivot Chord Mod - DONE