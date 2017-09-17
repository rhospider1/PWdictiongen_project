from itertools import chain, combinations

guessed_password_input = "password123"
guessed_passwordaslist = list(guessed_password_input)
min_pw_length = 5
max_pw_length = 10

master_list = []

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
    print(master_list)
else:
    print("Program aborted")