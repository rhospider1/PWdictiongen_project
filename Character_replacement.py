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
    password_length = len(password)
    countervar = 1
    count_max = 10
    first_char_counter = 0
    second_char_counter = 1
    third_char_counter = 2
    fourth_char_counter = password_length
    second_iter = []

    for an_chars in alpha_num:
        second_iter.append(list(chain(password[first_char_counter:second_char_counter], an_chars, password[third_char_counter:fourth_char_counter])))
        countervar += 1
        if countervar == count_max:
            #first_char_counter += 1
            second_char_counter += 1
            #third_char_counter += 1
            #fourth_char_counter +=1

            second_iter.append(list(chain(password[first_char_counter:second_char_counter], an_chars, password[third_char_counter:fourth_char_counter])))

    return second_iter
    #print(countervar)

#pprint.pprint(char_sub_first(guessedpwlist))
pprint.pprint(char_sub_rest(guessedpwlist))


