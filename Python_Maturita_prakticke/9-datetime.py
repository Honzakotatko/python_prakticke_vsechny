from datetime import datetime, timedelta
"""
now = datetime.now()

print(f"Datum a cas: {now}")
print(f"Cas: {now.time()}")
print(f"Datum: {now.date()}")
"""
"""
now = datetime.now()
cas = datetime.strftime(now,"%d.%m.%Y")

print(cas)
"""
"""
text = "24.12.2025"
cas = datetime.strptime(text, "%d.%m.%Y")

print(cas)
"""

now = datetime.now()

za_tyden = now + timedelta(days=7)
print(f"Za tyden: {za_tyden}")

vcera = now - timedelta(days=1)
print(f"Vcera: {vcera}")