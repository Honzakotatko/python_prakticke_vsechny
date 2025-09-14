slovnik = {"Jmeno": "Honza", "Vek": 18, "Obor": "IT"}

slovnik["Skola"] = "SPSMB"

slovnik["Jmeno"] = "Honza"

slovnik["Vek"] = 25
"""
for klice in slovnik:
    print(klice)
    
for hodnoty in slovnik.values():
    print(hodnoty)
"""
for klic_hodnota in slovnik.items():
    print(klic_hodnota)
    
"""
if "Jmeno" in slovnik:
    print(f"Jmeno: {slovnik['Jmeno']}")
    
else:
    print("Jmeno neni v sloviku")
    
del slovnik["Jmeno"]

if "Jmeno" in slovnik:
    print(f"Jmeno: {slovnik['Jmeno']}")
    
else:
    print("Jmeno neni v sloviku")
"""