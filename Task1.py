import random

def play_hangman():
    words = ["apple", "python", "planet", "hangman", "bridge"]  # 5 predefined words
    secret = random.choice(words).lower()
    guessed = ['_'] * len(secret)
    attempts_left = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    while attempts_left > 0 and '_' in guessed:
        print()
        print("Word: " + ' '.join(guessed))
        print("Attempts left:", attempts_left)
        if guessed_letters:
            print("Guessed letters:", ', '.join(guessed_letters))
        else:
            print("Guessed letters: None")
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in secret:
            for i in range(len(secret)):
                if secret[i] == guess:
                    guessed[i] = guess
            print("Good guess!")
        else:
            attempts_left -= 1
            print("Wrong guess.")

    if '_' not in guessed:
        print()
        print("Congratulations! You guessed the word:", secret)
    else:
        print()
        print("Game over. The word was:", secret)

if __name__ == "__main__":
    play_hangman()