# Forgotten password generator
# Creates iterations of password that gradually move further away from the original guess
# Author Tom Moore


from itertools import chain
import pprint

guessedpw = "password123"
alpha_num = ["a", "b", "c", "d", "e", "f"]


guessedpwlist = list(guessedpw)

def char_sub_first(password):
    first_iter = []
    for an_chars in alpha_num:
        first_iter.append(list(chain(an_chars, password[1:])))
    return first_iter

def char_sub_rest(password):
    password_length = len(password)
    #count_thing = 1
    first_char_counter = 0
    second_char_counter = 1
    third_char_counter = 2
    fourth_char_counter = password_length
    #first_char = password[first_char_counter]
    #continuation_char = password[continuation_char_counter:]
    second_iter = []
    for an_chars in alpha_num:
        second_iter.append(list(chain(password[first_char_counter:second_char_counter], an_chars, password[third_char_counter:fourth_char_counter])))
        #something to with starting and stopping in the right place [1:2]
            #count_thing += 1
        #first_char_counter += 1
        second_char_counter += 1
        third_char_counter += 1
        #fourth_char_counter +=1
    return second_iter


pprint.pprint(char_sub_rest(guessedpwlist))


