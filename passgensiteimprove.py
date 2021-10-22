import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
length = int(input("Length of password? "))
password =  "".join(choice(characters) for x in range(length))
print(password)