hash_table = {}

def simple_hash(value):
    return len(value) % 10  # jednoduchý hash: délka řetězce mod 10

def insert(value):
    key = simple_hash(value)
    if key not in hash_table:
        hash_table[key] = []
    hash_table[key].append(value)

# Příklad
insert("pes")
insert("auto")
insert("kočka")
print(hash_table)