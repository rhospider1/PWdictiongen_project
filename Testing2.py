from itertools import chain, combinations

min_pw_length = 4


def powerset(iterable):
    master_list = []
    s = list(iterable)
    x = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    for items in x:
        if len(items) > min_pw_length:
            master_list.append(items)
    return master_list

print(powerset("password"))