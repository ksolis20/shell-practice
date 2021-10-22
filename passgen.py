import string
from random import *
characters = string.ascii_letters + string.digits + string.punctuation
def gen_password():
	length = int(input("Length of password? "))
	password = []
	for x in range(length):
		password.append(choice(characters))
	print("".join(password))
gen_password()