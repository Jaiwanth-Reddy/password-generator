import string as s
from random import choice as c
from random import randint as r

length = int(input('Enter length of required password\n'))

lowercase = [i for i in s.ascii_lowercase]
uppercase = [i for i in s.ascii_uppercase]
symbols = [i for i in s.punctuation]
digits = [i for i in s.digits]

data = [lowercase,uppercase,symbols,digits]

part1,part2 = '',''

for i in range(length - 4):
    a = r(0,3)
    b = c(data[a])
    part1 += b

for i in range(0,4):            # part two of string to ensure
    b = c(data[i])              # each category has at least
    part2 += b                  # one element in the password

temp = list(part1)

while (part2 != ''):
    t = part2[0]                # each character of part2 being
    part2 = part2[1:]           # added into random positions
    temp.insert(r(0,len(temp)), t)  # of part1

final = ''

for i in temp:
    final += str(i)

print(final) 