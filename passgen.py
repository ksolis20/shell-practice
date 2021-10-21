import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_random_password():
	length = int(input("How long do you want your password? "))
	random.shuffle(characters)
	password = []
	for x in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)

	print("".join(password))


generate_random_password()