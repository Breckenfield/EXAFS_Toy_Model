import Functions
import unittest

class TestFunctions(unittest.TestCase):
    def test_CheckMaterialInput(self):
        self.assertTrue(Functions.CheckMaterialInput([1],[1],[1],[1]))
        self.assertFalse(Functions.CheckMaterialInput([],[1],[1],[1]))
        self.assertFalse(Functions.CheckMaterialInput([1],[1,2],[1],[1]))
        self.assertFalse(Functions.CheckMaterialInput([1],[1],[1,2],[1]))
        self.assertFalse(Functions.CheckMaterialInput([1],[1],[1],[1,2]))

if __name__ == '__main__':
    unittest.main()