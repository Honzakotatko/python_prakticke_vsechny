for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 2 == 0 and fizzbuzz % 5 == 0:
        print("rizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    elif fizzbuzz % 2 == 0:
        print("rizz")
        continue

    print(fizzbuzz) 