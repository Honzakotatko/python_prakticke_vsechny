from multiprocessing import Process

def soucet(n):
    vysledek = sum(range(1, n + 1))
    print(f"Vysledek: {vysledek}")
    
vlakno1 = Process(target=soucet, args=(10, ))
vlakno2 = Process(target=soucet, args=(5, ))

vlakno1.start()
vlakno2.start()

vlakno1.join()
vlakno1.join()

print("Konec programu")
