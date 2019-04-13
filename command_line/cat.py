import sys

for arg in sys.argv:
    file_input = open(arg, 'r')
    s = file_input.read()
    print(s)
    file_input.close()
    