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
    count_thing = 0
    count_max = 1
    first_char_counter = 0
    second_char_counter = 1
    third_char_counter = 2
    fourth_char_counter = password_length
    #first_char = password[first_char_counter]
    #continuation_char = password[continuation_char_counter:]
    second_iter = []
    while count_thing < count_max:
        for an_chars in alpha_num:
            count_thing += 1
            second_iter.append(list(chain(password[first_char_counter:second_char_counter], an_chars, password[third_char_counter:fourth_char_counter])))
    else:
        first_char_counter += 1
        second_char_counter += 1
        second_iter.append(list(chain(password[first_char_counter:second_char_counter], an_chars,
                                      password[third_char_counter:fourth_char_counter])))
        #third_char_counter += 1
        #fourth_char_counter +=1
    return second_iter
    #print(count_thing)


pprint.pprint(char_sub_rest(guessedpwlist))


