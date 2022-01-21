import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None), None) # test when null is given as input the output is null.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when Hello is given as input the output is Bonjour.
        self.assertNotEqual(english_to_french('Hello'), 'Hello')  # test when Hello is given as input the output is Bonjour.
       

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(None), None) # test when null is given as input the output is null.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when Bonjour is given as input the output is Hello.
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour') # test when Bonjour is given as input the output is not Bonjour.
       
unittest.main()
