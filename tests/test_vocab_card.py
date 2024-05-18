import unittest
from ankivocab.vocab_card import VocabCard

class TestVocabCard(unittest.TestCase):
    def test_vocab_card_creation(self):
        card = VocabCard(
            "example", 
            "noun", 
            "a representative form or pattern", 
            "This is an example sentence.", 
            "a representative form or pattern",
            ["example1.jpg", "example2.jpg"],
            "[ˈɛɡzæmpəl]",
            "example.mp3",
            ""
        )
        self.assertEqual(card.word, "example")
        self.assertEqual(card.gender, "noun")
        self.assertEqual(card.info, "a representative form or pattern")
        self.assertEqual(card.context, "This is an example sentence.")
        self.assertEqual(card.definition, "a representative form or pattern")
        self.assertEqual(card.pictures, ["example1.jpg", "example2.jpg"])
        self.assertEqual(card.pronunciation, "[ˈɛɡzæmpəl]")
        self.assertEqual(card.recording, "example.mp3")
        self.assertEqual(card.test_spelling, "")

if __name__ == "__main__":
    unittest.main()
