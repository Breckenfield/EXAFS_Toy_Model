import functions
import unittest

class TestFunctions(unittest.TestCase):
    def test_CheckMaterialInput(self):
        self.assertTrue(functions.CheckMaterialInput([1],[1],[1],[1]))
        self.assertFalse(functions.CheckMaterialInput([],[1],[1],[1]))
        self.assertFalse(functions.CheckMaterialInput([1],[1,2],[1],[1]))
        self.assertFalse(functions.CheckMaterialInput([1],[1],[1,2],[1]))
        self.assertFalse(functions.CheckMaterialInput([1],[1],[1],[1,2]))
    
    def test_LoadMaterialInput(self):
        materialInfo = functions.LoadMaterialInfo("test.json")
        materialName = "Test"
        material = materialInfo[materialName]
        self.assertEqual(len(materialInfo), 1)
        self.assertEqual(material["Symbol"],"Tst")
        self.assertEqual(material["RadiusDistance"], [1,2])
        self.assertEqual(material["NumberOfAtoms"], [1,2])
        self.assertEqual(material["Temperature"], 300)
        self.assertEqual(material["AtomicMass"], [1,2])
        self.assertEqual(material["EinsteinTemperature"], [300,400])

if __name__ == '__main__':
    unittest.main()