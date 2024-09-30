import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(Calculator.add(4, 5), 9)
    
    
    def test_subtract(self):
        self.assertEqual(Calculator.subtract(4, 2), 2)
    
    
    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 2), 4)
    
    
    def test_divide(self):
        self.assertEqual(Calculator.divide(4, 2), 2)
    
    
    if __name__ == "__main__":
        unittest.main
        
        
        

