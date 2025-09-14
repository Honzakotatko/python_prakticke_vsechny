"""
Tkinter

Standardní knihovna pro tvorbu GUI
Je součástí běžné instalace Pythonu
Slouží jako rozhraní k nástroji Tk, který je multiplatformní, umožňuje vytvářet okna, dialogy, tlačítka, textová pole, ...

"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Moje prvni aplikace")
root.geometry("400x300")
"""
label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(pady=20)

clicks = 0

def clicked():
    global clicks
    clicks+=1
    label.config(text="Stisknuto: " + str(clicks))

button = tk.Button(root, text="Klikni", command=clicked)
button.pack(pady=10)
"""

entry = tk.Entry(root, width=30, fg="green")
entry.pack(pady=10)

def vypis_vstup():
    vstup = entry.get()
    label.config(text=f"Zadal jsi {vstup}")
    messagebox.showerror("Informace", "Toto je informační okno")

button = tk.Button(root, text="Zobraz vstup", command=vypis_vstup)
button.pack(pady=5)

label = tk.Label(root, text="Výsledek bude zde")
label.pack(pady=10)

def klavesa_stisknuta(event):
    print(f"Stiknuta klavesa: {event}")
    
#root.bind("<Motion>", klavesa_stisknuta)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nový")
file_menu.add_command(label="Otevřít")
file_menu.add_separator()
file_menu.add_command(label="Ukončit", command=root.quit)
menu_bar.add_cascade(label="Soubor", menu=file_menu)

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

canvas.create_line(0, 0, 300, 200, fill="blue", width=3)
canvas.create_rectangle(50, 50, 150, 150, fill="red")

root.mainloop()