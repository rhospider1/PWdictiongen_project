from itertools import permutations

guessed_password_input = "password123"

def perms(password):
    return ["".join(i) for i in permutations(password)]

x=perms(guessed_password_input)

perms_file = open("perms.txt", "w")

perms_file.write(str(x))
perms_file.close()



