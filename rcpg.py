from midiutil.MidiFile import MIDIFile

def addChord(midiFile, track, channel, pitches, time, duration, volume):
    for pitch in pitches:
        midiFile.addNote(track, channel, pitch, time, duration, volume)

class ChordError(Exception):
    def __init__(self, chord, message):
        self.chord = chord
        self.message = "%s: %s" % (chord, message)
    def __str__(self):
        return repr(self.message)

class ChordWeightError(Exception):
    def __init__(self, chord, message):
        self.chord = chord
        self.message = "%s: %s" % (chord, message)
    def __str__(self):
        return repr(self.message)

class ChordMapError(Exception):
    def __init__(self, chords):
        self.chords = chords
        self.message = "These chords are mapped to but not mapped from:" + str(self.chords)
    def __str__(self):
        return repr(self.message)

class ChordMap(object):
    def __init__(self):
        self.chords = {}
    def isChordValid(self, chord):
        # validate input
        areAllNotesValid = all([type(n) == int and n >= 0 and n < 128 for n in chord])
        return type(chord) == tuple and areAllNotesValid
    def isWeightValid(self, weight):
        return type(weight) == int and weight > 0
    def addChord(self, chord, nextChords):
        for c in nextChords:
            if len(c) != 2:
                raise ChordWeightError(c, "Must include weight before each chord")
            if not self.isWeightValid(c[0]):
                raise ChordWeightError(c, "Weight must be int and > 0")
        if not self.isChordValid(chord) or not all([self.isChordValid(c[1]) for c in nextChords]):
            raise ChordError(chord, "Chord must be tuple and notes must be int >= 0 and < 128")
        self.chords[chord] = nextChords
    def getUnmappedChords(self):
        pass
    def generateProgression(self, length, start):
        pass

