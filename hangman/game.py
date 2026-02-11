from hangman_art import STAGES

class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.display = ["_"] * len(word)
        self.guessed_letters = set()
        self.lives = len(STAGES) - 1

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return "already"

        self.guessed_letters.add(letter)

        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.display[i] = letter
            return "correct"
        else:
            self.lives -= 1
            return "incorrect"

    def is_won(self):
        return "_" not in self.display

    def is_lost(self):
        return self.lives == 0
