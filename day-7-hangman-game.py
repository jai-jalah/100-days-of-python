import random

hanger = '''
  +---+
  |   |
      |
      |
      |
      |
========='''
body_part_list = ["|", "O", "|", "/", "\\", "/", "\\"]
counter = -1
word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)
answer = list(random_word)
blank = "_"
blank_answer = []
body_parts_used = []

for i in range(len(answer)):
    blank_answer.append(blank)

if counter != len(answer):
    guess = input("Guess a letter.\n").lower()
    counter += 1

if guess in random_word:
    print()
else:
    print("That was incorrect.")
    print(" ".join(blank_answer))
    body_parts_used.append(body_part_list[counter + 1])
    print(body_parts_used)


print(hanger)
