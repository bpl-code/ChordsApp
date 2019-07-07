#Chords Alt Version
# -*- coding: utf-8 -*-
#A program that helps you write chord progressions and modulations

class circleOfFifths():
    def __init__(self):
        self.keyNames = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B']
        self.keyScales = {'C' : ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'], 'C#' : ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#', 'C#'],\
        'Db' : ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db'], 'D' : ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D'],\
        'D' : ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D'], 'D#' : ['D#', 'E#', 'F##', 'G#', 'A#', 'B#', 'C##', 'D#'],\
        'Eb' : ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'], 'E' : ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'],\
        'F' : ['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F'], 'F#' : ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#', 'F#'],\
        'Gb' : ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F', 'Gb'], 'G' : ['G', 'A','B', 'C', 'D', 'E', 'F#', 'G'],\
        'G#' : ['G#', 'A#', 'B#', 'C#', 'D#', 'E#', 'F##', 'G#'], 'Ab' : ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab'],\
        'A' : ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A'], 'A#' : ['A#', 'B#', 'C##', 'D#', 'E#', 'F##', 'G##', 'A#'],\
        'Bb' : ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'], 'B' : ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B']}
        self.keySignitures = {}

    def buildKeys(self):
        #Create key object
        for key in self.keyNames:
            self.keySignitures[key] = keys(key, self.keyScales[key])

    def getKey(self, keyName):
        return key[keyName]



class keys():
    def __init__(self, keyName, scale):
        self.keyName = keyName
        self.scale = scale
        self.chordSymbols = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']

    def getScale(self):
        return self.scale

    def getChords(self):
        chords = []
        for i in range(7):
            chords.append(self.scale[i] + self.chordSymbols[i])
        return chords
