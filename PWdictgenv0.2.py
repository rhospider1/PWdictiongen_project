# Forgotten password generator
# Creates iterations of password that gradually move further away from the original guess
# Author Tom Moore

from itertools import chain, combinations
import os
guessed_password = "Password_15"

def muddler(guess):
    password_length = range(0, len(guess))
    pw_list = list(guess)
    for i in pw_list:
        if str.islower(i) == True:
            lower_chars = i
            for x in lower_chars:
                convert_to_upper = x.upper()

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    x = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    x_string = list(x)
    x_string_join = "".join(x_string)
    print(x)
    #power_set = open('powersetoutput2.txt', 'w')
    #power_set.write(x_string_join)
    #power_set.close()

powerset(guessed_password)