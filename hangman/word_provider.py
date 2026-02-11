import random

class WordProvider:
    def __init__(self):
        self.words = [
            "python", "developer", "hangman", "algorithm",
            "function", "variable", "object", "software"
        ]

    def get_random_word(self):
        return random.choice(self.words)
