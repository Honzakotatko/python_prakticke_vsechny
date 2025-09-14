"""
def fibonacci_recursive(n):
    if n == 1:
          return[0]
    elif n ==2:
          return [0 , 1]
    else:
         seq = fibonacci_recursive(n - 1)
         seq.append(seq[-1] + seq[-2])
         return seq
    
pocet = int(input("Zadejte pocet cisel Fibonacciho posloupnosti:"))
if pocet <= 0:
     print("Pocet musi byt kladne cislo")
else:
     print(f"Fibonacciho posloupnost ({pocet} cisel): {fibonacci_recursive(pocet)}")

"""

def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
cisla = int(input("Zadej cislo:"))
for i in range(cisla):
    print(fibonacci(i))
    
