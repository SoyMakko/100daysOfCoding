from word_provider import WordProvider
from game import HangmanGame
from hangman_art import LOGO, STAGES

def main():
    print(LOGO)

    provider = WordProvider()
    word = provider.get_random_word()
    game = HangmanGame(word)

    while not game.is_won() and not game.is_lost():
        print("\n" + " ".join(game.display))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        result = game.guess_letter(guess)

        if result == "already":
            print("You already guessed that letter.")
        elif result == "incorrect":
            print(STAGES[len(STAGES) - 1 - game.lives])
            print(f"'{guess}' is not in the word.")

    if game.is_won():
        print("\n🎉 YOU WIN!")
    else:
        print(f"\n💀 YOU LOSE! The word was '{word}'.")

if __name__ == "__main__":
    main()
