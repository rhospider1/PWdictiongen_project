# Forgotten password generator
# Creates iterations of password that gradually move further away from the original guess
# Author Tom Moore

from itertools import chain, combinations
import os
# Master list variable for all iterations stored as lists
master_list = []

#specify the minimum word length:
print("Welcome to my iteration of a password muddler")
min_pw_input = input("What is the minimum password length? (if not known put 1) ")
min_pw_length = int(min_pw_input)
print("The minimum password length is set at " + min_pw_input + ".")
max_pw_input = input("What is the maximum password length? (if not known enter X) ")

if max_pw_input == "x":
    max_pw_length = 20
else:
    max_pw_length = int(max_pw_input)

print("The maximum password length is set at " + str(max_pw_length) + ".")

guessed_password_input = input("What is your best guess at the existing password? (for unknown characters insert *)")
print("The original guessed password is " + guessed_password_input + ".")
guessed_passwordaslist = list(guessed_password_input)


def muddler(guess):
    password_length = range(0, len(guess))
    pw_list = list(guess)
    for i in pw_list:
        if str.islower(i) == True:
            lower_chars = i
            for x in lower_chars:
                convert_to_upper = x.upper()

#creates a powerset of the existing password, taking into account min and max lengths
def powerset(iterable):
    s = list(iterable)
    x = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    for items in x:
        if len(items) > min_pw_length:
            master_list.append(items)

    #power_set = open('powersetoutput2.txt', 'w')
    #power_set.write(x_string_join)
    #power_set.close()

#add list of called functions to this
proceed_yn = input("Do you wish to generate a password list now? (y/n)")
if proceed_yn == "Y" or "y" or "Yes" or "yes" or "YES":
    powerset(guessed_password_input)
else:
    print("Program aborted")