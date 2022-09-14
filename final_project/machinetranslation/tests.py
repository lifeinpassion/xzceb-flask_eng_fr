#from asyncio import start_unix_server
import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(' '), ' ')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Byebye')

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(' '), ' ')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('How are you?'), 'Bonjour')

unittest.main()
