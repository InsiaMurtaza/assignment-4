import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'developer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters:set = set()
    tries = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")

    while tries > 0:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            guessed_letters.add(guess)
            tries -= 1
            print(f"Wrong guess! Tries left: {tries}")

    if tries == 0:
        print(f"Game Over! The word was: {word}")

def main():
    hangman()

if __name__ == "__main__":
    main()