print('''
  .,.,
           (((((())
          ((('.  .`)
          ((G   \ |)             ,~~~,
      __.(((`   ~ , --. __      ,~~~~~,
 _---'\_\/.((\.:v:   \ /_/`--_ (  )(  ))
<._   __(__ .| `"'. __)__    _.))(  )(((
   `-/_/ \_\ `---' /_/_\_|.-'  (( )(  )))         \\\
       `-------\\\-----'        ))( )(((         \,))))
               \\\`-(          ((  )( )))         (!\/
                `--. \       ---))(  (((---       /!,'
                    \ \    /   ((  )  )))   \    /.,.|
                     \ \  /  `  ))(  ((( '\  \  /.,!.|
                      \ \/  / \((  )  ))) )\  \/.,::.|
                       \   /   \         |  \  |,::!.|
                        \_/     \        |   \_|:.:!!|
                                 )       |   |.|:::!!|
                                /        |   |.|!::!!|
                               /         |   |.|!:::!|
                              /  Y       \   `~|!!::!|
                             '   (        \    |!!::.|
                             `    `.       \   |.!.:.|
                              \     `.      \  |.!...|
                               \     |`.     \ |...!.|
                                \    |   \    \|...!.|
                                 )   )    )    |..!!.|
                                /   (    /    /|!.!!.|
                               |     \  |    / |!.!!.|
                                \    /  |   /  |!_~-'
ejm98                            \  /   |  /   `~
(with thanks to                   )(    ) (
a:f for his severed head         (__)  (__ `.
and jaz for the veil)                     `._`..
''')

print("Ahoy, matey! Welcome to Treasure Island!")
print("Yar' mission is ta find tha' deep treasure..\n")

choice1 = input("No time ta' waste! You see that divergin' path? Would ya like to go down the left one, or the right one?\n").lower()

if choice1 == "left":
  choice2 = (input("\nHmmm, looks like you've arrived at a simmering lava lake. Would ya like to use this new swimsuit I found, or wait? Type 'swim', or 'wait'.\n")).lower()
  if choice2 == "wait":
    choice3 = input("\nWell blow me down, yar' not half bad! It's not over yet though, avast ye! Ya see those dastardly, giant doors? Ya gotta choose one to find the deep treasure. Quick, choose! Red, yellow, blue.. or the secret one?\n").lower()
    if choice3 == "yellow":
      print("\nGood thinkin matey, ya' did it! Time for some hornswagglin!")
    elif choice3 == "red":
      print("\nDarn! Ya got burned by fiyaa! Game over for you, heartie!")
    elif choice3 == "blue":
      print("\nArghhh. You were eaten by a dastardly beast! Game over, and thanks for feedin' my pet.")
    else:
      print("\nWhy would ya ever think a secret door would be the answer! It's over for ya'!")
  else:
    print("\nDarn! Why would you think the swimsuit would protect you against the lava trout! Don't say I didn't warn ya.")
else:
  print("\nWell done! Ya fell into quicksand. Game oveeeerrrrr.")

print('''
    .d88b.
    88  88
    `8bd8'
     `88'
 g888SEAL888g
      88
      88
      88
     d88b
    d8888b
''')
