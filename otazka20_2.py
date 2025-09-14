import tkinter as tk
from tkinter import ttk
 
# ==========================
# Model – logika kalkulačky
# ==========================
class CalculatorModel:
    def __init__(self):
        # Uchovává aktuální výraz (řetězec)
        self.expression = ""
    def add_to_expression(self, value):
        """Přidá hodnotu (číslo nebo operátor) k aktuálnímu výrazu."""
        self.expression += str(value)
    def clear_expression(self):
        """Vymaže aktuální výraz."""
        self.expression = ""
    def evaluate_expression(self):
        """Vyhodnotí výraz a vrátí výsledek. Pokud dojde k chybě, nastaví výraz na 'Error'."""
        try:
            # Použijeme vestavěnou funkci eval pro vyhodnocení výrazu.
            result = eval(self.expression)
            self.expression = str(result)
        except Exception:
            self.expression = "Error"
        return self.expression
 
# ==========================
# View – uživatelské rozhraní
# ==========================
class CalculatorView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulačka MVC")
        self.geometry("300x400")
        self.resizable(0, 0)  # Zamezení změny velikosti okna
 
        # Proměnná pro zobrazení výrazu a výsledku
        self.expression_var = tk.StringVar()
 
        self.create_widgets()
 
    def create_widgets(self):
        # --- Vytvoření displeje ---
        display = ttk.Entry(self, textvariable=self.expression_var, font=("Arial", 24), justify="right")
        display.pack(fill="x", padx=10, pady=10)
 
        # --- Rámec pro tlačítka ---
        buttons_frame = ttk.Frame(self)
        buttons_frame.pack(expand=True, fill="both")
 
        # Definice tlačítek v mřížce (řádky a sloupce)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]
 
        # Vytvoření tlačítek pomocí cyklu
        for row_index, row in enumerate(buttons):
            for col_index, button_text in enumerate(row):
                # Přiřadíme každému tlačítku callback funkci, která předá text tlačítka.
                btn = ttk.Button(buttons_frame, text=button_text,
                                 command=lambda text=button_text: self.on_button_click(text))
                btn.grid(row=row_index, column=col_index, sticky="nsew", padx=5, pady=5)
 
        # Tlačítko pro vymazání (Clear)
        clear_button = ttk.Button(self, text="C", command=lambda: self.on_button_click("C"))
        clear_button.pack(fill="x", padx=10, pady=5)
 
        # Zajistíme, aby se buňky mřížky roztahovaly rovnoměrně
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
            buttons_frame.rowconfigure(i, weight=1)
 
    # Tuto metodu nastaví Controller – ten se přihlásí jako callback.
    def set_button_callback(self, callback):
        self.button_callback = callback
 
    # Metoda, která se volá při stisknutí tlačítka
    def on_button_click(self, value):
        if hasattr(self, "button_callback"):
            self.button_callback(value)
 
    # Metoda pro aktualizaci displeje
    def update_display(self, text):
        self.expression_var.set(text)
 
# ==========================
# Controller – spojuje Model a View
# ==========================
class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Nastavíme callback z View na metodu v Controlleru
        self.view.set_button_callback(self.handle_button_click)
 
    def handle_button_click(self, value):
        """
        Metoda reagující na stisk tlačítka.
         - Pokud je stisknuto "C", vymaže výraz.
         - Pokud je stisknuto "=", vyhodnotí výraz.
         - Jinak přidá hodnotu (číslo či operátor) k výrazu.
        """
        if value == "C":
            self.model.clear_expression()
            self.view.update_display(self.model.expression)
        elif value == "=":
            result = self.model.evaluate_expression()
            self.view.update_display(result)
        else:
            self.model.add_to_expression(value)
            self.view.update_display(self.model.expression)
 
# ==========================
# Hlavní funkce – spuštění aplikace
# ==========================
def main():
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    view.mainloop()
 
if __name__ == "__main__":
    main()