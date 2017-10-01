# Forgotten password generator
# Creates iterations of password that gradually move further away from the original guess
# Author Tom Moore


from itertools import chain
import string
import pprint

password = "password123"
alpha_num = list(string.printable)
second_iter = []
password_length = len(password)
countervar = 1
count_max = 26
first_char_counter = 0
second_char_counter = 1
third_char_counter = 2
fourth_char_counter = password_length
second_iter = []

for an_chars in alpha_num:
    second_iter.append(list(chain(password[first_char_counter:second_char_counter], an_chars,
                                  password[third_char_counter:fourth_char_counter])))

pprint.pprint(second_iter)