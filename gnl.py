import sys

def get_next_line():
    file = open(sys.argv[1], 'r')
    for line in file:
        print(line, end='')
    file.close()

get_next_line()