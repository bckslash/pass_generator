import random
import os

numbers = "0123456789"
upper = "ABCDEFGHIJKLMNOPRQSTVWUXYZ"
lower = upper.lower()
symbols = ")(}{][></!?@#$%^&*-=+;:,."
temp = ""

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

clear()
print("======== password generator ========")

choice_seed = input("Do you want to use seed [Y/n]\n")
if choice_seed.lower() == 'y':
	is_seed = True
	clear()
	seed = input("Enter seed: ")
	clear()
else:
	seed = None
	is_seed = False
	clear()

choice_nums = input("Do you want to use numbers [Y/n]\n")

if choice_nums.lower() == 'y':
	is_numbers = True
	clear()
else:
	is_numbers = False
	clear()

choice_characters = input("Do you want to use characters [Y/n]\n")

if choice_characters.lower() == 'y':
	choice_characters_style = input("[1]for only upper / [2]for only lower / [12]for both\n")

	if choice_characters_style == '1':
		is_upper, is_lower = True, False

	if choice_characters_style == '2':
		is_lower, is_upper = True, False

	if choice_characters_style == '12':
		is_lower, is_upper = True, True
	clear()
else:
	is_lower, is_upper = False, False
	clear()

choice_symbols = input("Do you want to use symbols [Y/n]\n")

if choice_symbols.lower() == 'y':
	is_symbols = True
	clear()
else:
	is_symbols = False
	clear()

lenght = input("How long the password will be: ")
if not lenght.isnumeric():
	print("not a number")
clear()
count = input ("How many passwords will be generated: ")
if not count.isnumeric():
	print("not a number")
clear()

if is_numbers:
	temp += numbers

if is_lower:
	temp += lower

if is_upper:
	temp += upper

if is_symbols:
	temp+= symbols

if is_seed:
	random.seed(seed)

if is_numbers == False and is_symbols == False and is_upper == False and is_lower == False:
	print("======== ERROR! Password can't be generated! ========")
else:
	print("======== YOUR PASSWORDS ========\n")

	with open('pass.txt', 'a') as f:
		f.write(f"Lenght: {lenght} / Count: {count} / Numbers: {is_numbers} / Lower: {is_lower} / Upper: {is_upper} / Symbols: {is_symbols} / Seed: {is_seed}, {seed}\n")

		for i in range (int(count)):
			password = "".join(random.sample(temp, int(lenght)))
			print(password)
			f.write(password + '\n')
		f.write('\n')