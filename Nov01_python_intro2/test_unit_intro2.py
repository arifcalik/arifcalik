import unittest
from python_intro2 import arrayCheck, stringBits, doubleChar, count_evens

class TestIntro2(unittest.TestCase):
    def setUp(self) -> None:
        self.testList = []
        self.testString = '' 
        return super().setUp()
    
    #even though not funtional here better to have for future use
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_arrayCheck(self):
        #empty list - default in setup!
        result = arrayCheck(self.testList)
        #False is expected result
        self.assertEqual(result, False) 

        self.testList = [1, 1, 2, 0, 1, 3, 2, 1, 2, 1, 2, 4, 3, 1, 2,]
        result = arrayCheck(self.testList)
        self.assertEqual(result, False)
  
        #assertTrue
        self.testList = [3, 2, 1, 2, 3]
        result = arrayCheck(self.testList)
        #False is expected result
        self.assertTrue(result)               
    
    def test_stringBits(self):
        #empty testString! - default
        result = stringBits(self.testString)
        self.assertEqual(result, '')

        self.testString = 'Wwworldlldde'
        result = stringBits(self.testString)
        self.assertEqual(result, 'Wwrdld')
        

    def test_doubleChar(self):
        self.testString = 'Hi-There'
        result = doubleChar(self.testString)
        self.assertEqual(result, 'HHii--TThheerree')
        # how about sending empty string
        self.testString = ''
        result = doubleChar(self.testString)
        self.assertEqual(result, '')        

    def test_count_evens(self):
        self.testString = [-1, 1, 7, 3, -123, 23, 67, 7,]
        result = count_evens(self.testString)
        self.assertEqual(result, 0)
        '''
        how about sending empty list!
        '''
        self.testString = []
        result = 0  #as expected
        self.assertEqual(result, 0)

    @unittest.skip("In progress") 
    def test_skip(self):
        pass

