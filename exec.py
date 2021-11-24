import sys
import re

reversed = str(sys.argv[1:])

def ugh():
    string1 = " ".join(re.findall("[a-zA-Z]+", reversed))
    rev = string1[::-1]
    print(rev.swapcase())

ugh()