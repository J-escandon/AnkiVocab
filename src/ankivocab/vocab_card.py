class VocabCard:
    def __init__(self, word, gender=None, info=None, context=None, definition=None,
                 pictures=None, pronunciation=None, recording=None, test_spelling=None):
        self.word = word
        self.gender = gender
        self.info = info
        self.context = context
        self.definition = definition
        self.pictures = pictures if pictures else []
        self.pronunciation = pronunciation
        self.recording = recording
        self.test_spelling = test_spelling

    def __repr__(self):
        return (f"Word: {self.word}\n"
                f"Gender: {self.gender}\n"
                f"Info: {self.info}\n"
                f"Context: {self.context}\n"
                f"Definition: {self.definition}\n"
                f"Picture: {', '.join(self.picture)}\n"
                f"Pronunciation (Recording and/or IPA): {self.pronunciation}\n"
                f"Recording: {self.recording}\n"
                f"Test Spelling? (y = yes, blank = no: {self.test_spelling}")

    def to_csv_row(self):
        return [
            self.word, self.gender, self.info, self.context, self.definition,
            ", ".join(self.pictures), self.pronunciation, self.recording, self.test_spelling
        ]