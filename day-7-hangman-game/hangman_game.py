import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)
counter = 0
chosen_word = random.choice(word_list)
ans = list(chosen_word)
blank = "_"
blank_ans = []

for i in range(len(ans)):
        blank_ans.append(blank)

while counter < 6:

    guess = input("Guess a letter.\n").lower()

    if guess in chosen_word:
        indices = [i for i, x in enumerate(ans) if x == guess]
        for indice in indices:
            blank_ans[indice] = guess
        print(" ".join(blank_ans))
        print(stages[counter])
        if blank_ans == ans:
            print("\nYou saved him!!")
            break
    else:
        counter += 1
        print("\nNope. Try another letter!\n")
        print(" ".join(blank_ans))
        print(stages[counter])
        if counter == 6:
            print("\nWell, I guess you couldn't save him. Maybe in another life...")
