#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#1. calculation = bill / people * (1 + tip / 100)
#2. round((calculation), 2))

print("Howdy! Welcome to the tip calculata'")

bill = float(input("How much ya say ya bill was? $"))
tip = float(input("Mmm, and the tip ya wanna pay on that - 10%, 12%, 15%? "))
split = float(input("And how many of ya are payin?? "))

result = float(round(bill / split * (1 + tip / 100), 2))

print(f"Well here ya go. Each one of ya's gon' have to pay ${result}!")
