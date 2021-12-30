import random
import hangman_art
import hangman_words

lives = 6
game_over = False

print(hangman_art.logo)
print(f"You have {lives} lives")

chosen_word = random.choice(hangman_words.word_list)
word_length = len((chosen_word))
# print(f"The answer is {chosen_word}")

display = []
for _ in range(word_length):
    display.append("_")

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess

    if guess not in chosen_word:
        lives -= 1
        if lives >= 1:
            print(f"You guessed {guess}. That's not in the word. You lose a life ({lives} lives remaining).")
        else:
            game_over = True
            print("All lives lost! You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(hangman_art.stages[lives])
