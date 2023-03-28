
import unittest
import os

class VariousAsserts(unittest.TestCase):
        
    def test_asserts(self):
        a = 100
        b = 200
#         self.assertEqual(a, b)   # a == b
        self.assertNotEqual(a, b)  # a!= b
        
        #self.asertTrue(a == b)  # True
        self.assertFalse(a == b) # False
        
        #self.assertIs(a, b)
        self.assertIsNot(a, b)
        
        #self.assertIsNone(a)
        self.assertIsNotNone(a)
        
        #self.assertNotIsInstance(a, int) #isinstance(a, int)
        self.assertIsInstance(a, int)     #notisinstance(a, int)
        
        #self.assertGreater(a, b)   # a > b
        self.assertLess(a, b)       # a < b
        
        
if __name__ == '__main__':
    unittest.main()
