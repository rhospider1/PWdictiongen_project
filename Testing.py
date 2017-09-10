from itertools import combinations
from itertools import chain

min_pw_length = 5


def powerset(iterable):
    s = list(iterable)
    x = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    x_string = list(x)
    for items in x_string:
        if len(x_string) > min_pw_length:
            print("".join(items))

powerset("password")