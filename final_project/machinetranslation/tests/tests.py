from asyncio import start_unix_server
import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(''), '')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(''), '')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

TestTranslator()
