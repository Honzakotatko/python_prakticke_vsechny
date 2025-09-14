import tkinter as tk

count = 0

def click():
    global count
    count +=1
    label.config(text=f"Pocet: {count}")
    
    
root = tk.Tk()
root.title("Jednoduchy Clicker")
root.geometry("800x400")

label = tk.Label(root, text=f"Pocet: {count}")
label.pack(pady=10)

button = tk.Button(root, text="Klikni me", command=click)
button.pack(pady=10)


root.mainloop()