import random

# Hangman stages (5 stages)
hangman_stages = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]

# Word list
mylist = ["carmel", "aitam", "arjun"]
hangchoice = random.choice(mylist)

# Initial placeholder
display = "_" * len(hangchoice)
print(display)

game_over = False
correct_letters = []
wrong_guesses = 0

while not game_over:
    guess = input("Enter the guess: ").lower()

    if guess in hangchoice:
        # Build new display string
        new_display = ""
        for letter in hangchoice:
            if letter == guess or letter in correct_letters:
                new_display += letter
            else:
                new_display += "_"
        display = new_display
        print(display)

        # Track correct guesses
        if guess not in correct_letters:
            correct_letters.append(guess)
    else:
        # Wrong guess → advance stage
        print(hangman_stages[wrong_guesses])
        wrong_guesses += 1

    # Win condition
    if "_" not in display:
        game_over = True
        print("🎉 You Won!")

    # Lose condition
    if wrong_guesses == len(hangman_stages):
        game_over = True
        print(" You Lost! The word was:", hangchoice)
