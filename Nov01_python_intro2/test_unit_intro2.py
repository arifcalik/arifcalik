import unittest
from python_intro2 import arrayCheck, stringBits, doubleChar, count_evens

class TestIntro2(unittest.TestCase):
    def test_arrayCheck(self):
        testList1 = [1, 1, 2, 0, 1, 3, 2, 1, 2, 1, 2, 4, 3, 1, 2,]
        result = arrayCheck(testList1)
        self.assertEqual(result, False)
    
    def test_stringBits(self):
        input = 'Wwworldlldde'
        result = stringBits(input)
        self.assertEqual(result, 'Wwrdld')

    def test_doubleChar(self):
        input = 'Hi-There'
        result = doubleChar(input)
        self.assertEqual(result, 'HHii--TThheerree')

    def test_count_evens(self):
        input = [-1, 1, 7, 3, -123, 23, 67, 7,]
        result = count_evens(input)
        self.assertEqual(result, 0)
        


