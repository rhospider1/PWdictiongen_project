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
    countervar = 0
    x = 2
    first_char_counter = 1
    first_iter = []
    while countervar < len(password):
        for an_chars in alpha_num:
            first_iter.append(list(chain(an_chars, password[first_char_counter:])))
            countervar += 1
            first_char_counter += 1
        return first_iter
    else:
        print("end of sequence")

#pprint.pprint(char_sub_first(guessedpwlist))


#This function iterates through the second character and then continues through all the rest of the letters
def char_sub_rest(password):
    password_length = len(password)
    countervar = 1
    count_max = 26
    first_char_counter = 0
    second_char_counter = 1
    third_char_counter = 2
    fourth_char_counter = password_length
    second_iter = []

    while countervar < 4:
        for an_chars in alpha_num:
            second_iter.append(list(chain(password[first_char_counter:second_char_counter], an_chars, password[third_char_counter:fourth_char_counter])))
        if second_char_counter < password_length:
            second_char_counter += 1
            third_char_counter += 1
            countervar += 1
        return second_iter

    else:
        print("End of all")
    print(second_iter)

    #print(countervar)


char_sub_rest(guessedpwlist)


