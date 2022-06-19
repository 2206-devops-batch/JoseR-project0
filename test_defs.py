import unittest
import Classes

class TestingMethods(unittest.TestCase):
    
    def test_contains_a_digit(self):
        result = Classes.contains_a_digit('qwertyuiopasdfghjklzxcvbnmm')
        self.assertFalse(result)
        
        result2 = Classes.contains_a_digit('qwert2yuio')
        self.assertTrue(result2)
    
    def test_enter_Y_N_to_proceed(self):
        result = Classes.enter_Y_N_to_proceed('test Y/N to proced')
        if result == 'Y' or result == 'N':
            self.assertTrue(result)
        else:
            self.assertNotEqual(result)
        
    def test_add_credentials(self):
        result = Classes.add_credentials()
        self.assertIsInstance(result ,Classes.password_manager)
        
        

if __name__ == '__main__':
    unittest.main()