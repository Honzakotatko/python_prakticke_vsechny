"""
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)



n = int(input("Zadejte cislo: "))
print(f"Faktorial cisla {n} se rovna {faktorial(n)}")
"""

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)


print(f"Faktorial cisla 5 je {faktorial(5)}")


def sum_args(*args):
    return sum(args)


print(f"soucet cisel 1, 2, 3, 4, 5, 6 je {sum_args(1, 2, 3, 4, 5, 6)}")

    