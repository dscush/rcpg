import unittest
import rcpg

class ChordMapTestCase(unittest.TestCase):
    def setUp(self):
        self.cm = rcpg.ChordMap()
        self.c = (50,54,57)
        self.f = (50,55,59)
        self.g = (49,52,57)
        self.a = (50,54,59)

class ChordValidityTestCase(ChordMapTestCase):
    def testKeyChordAsListRaisesChordError(self):
        self.assertRaises(rcpg.ChordError, self.cm.addChord, list(self.c), ((5,self.f),(4,self.g),(1,self.a)))
    def testNegativeNoteInKeyRaisesChordError(self):
        self.assertRaises(rcpg.ChordError, self.cm.addChord, (50,-3,59), ((5,self.f),(4,self.g),(1,self.a)))
    def testNoteTooHighInKeyRaisesChordError(self):
        self.assertRaises(rcpg.ChordError, self.cm.addChord, (50,130,59), ((5,self.f),(4,self.g),(1,self.a)))
    def testFloatNoteInKeyRaisesChordError(self):
        self.assertRaises(rcpg.ChordError, self.cm.addChord, (50,13.1,59), ((5,self.f),(4,self.g),(1,self.a)))
    def testNonNumberNoteInKeyRaisesChordError(self):
        self.assertRaises(rcpg.ChordError, self.cm.addChord, (50,'foo',59), ((5,self.f),(4,self.g),(1,self.a)))
    def testValueContainsChordAsListRaisesChordError(self):
        self.assertRaises(rcpg.ChordError, self.cm.addChord, self.c, ((5,self.f),(4,list(self.g)),(1,self.a)))
    def testNegativeNoteInValueRaisesChordError(self):
        self.assertRaises(rcpg.ChordError, self.cm.addChord, self.c, ((5,(50,-3,61)),(4,self.g),(1,self.a)))
    def testNoteTooHighInValueRaisesChordError(self):
        self.assertRaises(rcpg.ChordError, self.cm.addChord, self.c, ((5,(50,130,61)),(4,self.g),(1,self.a)))
    def testFloatNoteInValueRaisesChordError(self):
        self.assertRaises(rcpg.ChordError, self.cm.addChord, self.c, ((5,(50,13.1,61)),(4,self.g),(1,self.a)))
    def testNonNumberNoteInValueRaisesChordError(self):
        self.assertRaises(rcpg.ChordError, self.cm.addChord, self.c, ((5,(50,'foo',61)),(4,self.g),(1,self.a)))
    def testWeightAsFloatRaisesChordWeightError(self):
        self.assertRaises(rcpg.ChordWeightError, self.cm.addChord, self.c, ((5.5,self.f),(4,self.g),(1,self.a)))
    def testNegativeWeightRaisesChordWeightError(self):
        self.assertRaises(rcpg.ChordWeightError, self.cm.addChord, self.c, ((-5,self.f),(4,self.g),(1,self.a)))
    def testMissingWeightRaisesChordWeightError(self):
        self.assertRaises(rcpg.ChordWeightError, self.cm.addChord, self.c, ((self.f,),(4,self.g),(1,self.a)))
        self.assertRaises(rcpg.ChordWeightError, self.cm.addChord, self.c, (self.f,(4,self.g),(1,self.a)))
    def testEverythingValidRaisesNoErrors(self):
        try:
            self.cm.addChord(self.c,((5,self.f),(4,self.g),(1,self.a)))
        except rcpg.ChordError:
            self.fail()

