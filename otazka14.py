import random

dictionary = {}

def pridani(item):
    x = random.randint(1, 10)
    if x in dictionary:
        dictionary[x].append(item)
    else:
        dictionary[x] = [item]
        
pridani("kocicka")
pridani("pes")
print(dictionary)