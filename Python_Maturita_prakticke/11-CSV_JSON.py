"""
import json
"""
# Zapis JSON
"""
data = {"jmeno": "Adam", "vek": 18}

with open("soubor.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file)
"""
# Cteni JSON
"""
with open("soubor.json", encoding="utf-8") as json_file:
    data = json.load(json_file)

print(data)
"""
"""
import csv
"""
# Zapis CSV
"""
with open("soubor.csv", "w", newline="", encoding="utf-8") as csv_file:
    data = csv.writer(csv_file)
    
    data.writerow(["jmeno", "vek"])
    data.writerow(["Honza", "19"])
"""
# Cteni CSV
"""
with open("soubor.csv", newline="", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for i in reader:
        print(i)
"""