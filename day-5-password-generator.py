import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# 1. new list for letters, symbols, and numbers.
# 2. for letters in range(1, nr_letters + 1), select random letter and insert in new list.
# 3. same for nr_symbols and nr_numbers.
# 4. combine all the variables together into a randomised list and join the list.
# 5. print the password
letter_list = []
number_list = []
symbol_list = []
password_list = []

total_chars = nr_letters + nr_numbers + nr_symbols

if nr_letters > 0:
    for letter in range(0, nr_letters + 1):
        letter_list.append(letters[random.randint(0, 25)])

if nr_numbers > 0:
    for number in range(0, nr_numbers + 1):
        number_list.append(numbers[random.randint(0, 9)])

if nr_symbols > 0:
    for symbol in range(0, nr_symbols + 1):
        symbol_list.append(symbols[random.randint(0, 8)])

while len(password_list) < total_chars:
    if len(letter_list) > 0:
        password_list.append(letter_list[random.randint(0, len(letter_list) - 1)])
    if len(number_list) > 0:
        password_list.append(number_list[random.randint(0, len(number_list) - 1)])
    if len(symbol_list) > 0:
        password_list.append(symbol_list[random.randint(0, len(symbol_list) - 1)])

password = "".join(password_list)
print(f"Your new password is: {password}")
