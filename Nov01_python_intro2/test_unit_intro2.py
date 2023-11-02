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
    
    def test_empty_list_arrayCheck(self):
        #empty list - default in setup!
        result = arrayCheck(self.testList)
        #False is expected result
        self.assertEqual(result, False) 

    def test_sample_list_arrayCheck(self):
        self.testList = [1, 1, 2, 0, 1, 3, 2, 1, 2, 1, 2, 4, 3, 1, 2,]
        result = arrayCheck(self.testList)
        self.assertEqual(result, False)
  
    def test_sample_list_with_assertTrue_arrayCheck(self):
        #assertTrue
        self.testList = [3, 2, 1, 2, 3]
        result = arrayCheck(self.testList)
        #False is expected result
        self.assertTrue(result)               
    
    def test_empty_string_stringBits(self):
        #empty testString! - default
        result = stringBits(self.testString)
        self.assertEqual(result, '')

    def test_sample_string_stringBits(self):
        self.testString = 'Wwworldlldde'
        result = stringBits(self.testString)
        self.assertEqual(result, 'Wwrdld')
        

    def test_sample_string_doubleChar(self):
        self.testString = 'Hi-There'
        result = doubleChar(self.testString)
        self.assertEqual(result, 'HHii--TThheerree')

    def test_empty_string_doubleChar(self):        
        # how about sending empty string
        self.testString = ''
        result = doubleChar(self.testString)
        self.assertEqual(result, '')        

    def test_sample_list_count_evens(self):
        self.testList = [-1, 1, 7, 3, -123, 23, 67, 7,]
        result = count_evens(self.testList)
        self.assertEqual(result, 0)

    def test_empty_list_count_evens(self):        
        '''
        how about sending empty list!
        '''
        self.testList = []
        result = 0  #as expected
        self.assertEqual(result, 0)

    @unittest.skip("In progress") 
    def test_skip(self):
        pass

