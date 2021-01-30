rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]

player_choice = int(input("So you think you can beat me at RPS?? Bet! Type 0 to choose Rock, 1 to choose Paper, and 2 to choose Scissors!\n"))

while player_choice > 2:
   player_choice = int(input("You tryna invent a new move or somethin'? Try again, 0 to 2!\n"))

print(choices[player_choice])

print("--------------------------")

import random
comp_choice = random.randint(0, 2)

print(choices[comp_choice])

if player_choice == comp_choice:
    print("Wha! We can't just draw!! Hit restart, let's go again.")
elif player_choice == 0 and comp_choice == 2:
    print("Ughh, fine you win.")
elif player_choice > comp_choice:
    print("Ughh, fine you win.")
elif comp_choice == 0 and player_choice == 2:
    print("Boom! Told ya I'd win!")
else:
    print("Boom! Told ya I'd win!")
