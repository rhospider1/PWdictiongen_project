# Forgotten password generator
# Creates iterations of password that gradually move further away from the original guess
# Author Tom Moore

from itertools import chain, combinations
import pprint
import os

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

# Capitalise first letter and then last letter, then first two letters, then last two letters
def capitalise(password):
    capped_password = []
    capped_password.append(password.title())
    capped_password.append(password[0].title() + password[1].title() + password[2:])
    capped_password.append(password[:-1] + password[-1].title())
    capped_password.append(password[:-2] + password[-2].title() + password[-1].title())
    capped_password.append(password.upper())
    return capped_password

#creates a powerset of the existing password, taking into account min and max lengths
def powerset(iterable):
    master_list = []
    s = list(iterable)
    x = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    for items in x:
        if len(items) > min_pw_length:
            master_list.append(items)
    return master_list.join


# calls the functions and creates lists of outputs

output_list = []
proceed_yn = input("Do you wish to generate a password list now? (y/n)")
if proceed_yn == "Y" or "y" or "Yes" or "yes" or "YES":
    output_list.append(powerset(guessed_password_input))
    output_list.append(capitalise(guessed_password_input))
    pprint.pprint(output_list)
else:
    print("Program aborted")