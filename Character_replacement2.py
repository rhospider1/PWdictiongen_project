# Forgotten password generator
# Creates iterations of password that gradually move further away from the original guess
# Author Tom Moore


from itertools import chain
import string
import pprint

guessedpw = "password123"
alpha_num = list(string.printable)


guessedpwlist = list(guessedpw)

#This iterates through the first letter of the password and replaces it with all printable characters
def char_sub_first(password):
    first_iter = []
    for an_chars in alpha_num:
        first_iter.append(list(chain(an_chars, password[1:])))
    return first_iter

#This function iterates through the second character and then continues through all the rest of the letters
def char_sub_rest(password):
    password_iter = iter(password)
    next_iter = next(password_iter)next(alpha_num)
    else:


#pprint.pprint(char_sub_first(guessedpwlist))
pprint.pprint(char_sub_rest(guessedpwlist))



# second_iter.append(list(chain(password[first_char_counter:second_char_counter], an_chars, password[third_char_counter:fourth_char_counter])))
