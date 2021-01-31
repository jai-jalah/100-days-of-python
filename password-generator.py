import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# 1. new list for letters, symbols, and numbers.
# 2. for letters in range(1, nr_letters + 1), select random letter and insert in new list.
# 3. same for nr_symbols and nr_numbers.
# 4. combine all the variables together into a randomised list and join the list.
# 5. print the password
import random

letters_ans = []
symbols_ans = []
numbers_ans = []
ans = []

total = nr_letters + nr_symbols + nr_numbers

for letter in range(1, nr_letters + 1):
    letters_ans.append(letters[random.randint(0, nr_letters - 1)])

for symbol in range(1, nr_symbols + 1):
    symbols_ans.append(symbols[random.randint(0, nr_symbols - 1)])

for number in range(1, nr_numbers + 1):
    numbers_ans.append(numbers[random.randint(0, nr_numbers - 1)])

while len(ans) < total:
    ans.append(letters_ans[random.randint(0, len(letters_ans) - 1)])
    ans.append(symbols_ans[random.randint(0, len(symbols_ans) - 1)])
    ans.append(numbers_ans[random.randint(0, len(numbers_ans) - 1)])
