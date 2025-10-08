import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.configure(bg="#f0f0f0")

        self.expression = ""
        self.entry = tk.Entry(master, width=18, font=("Arial", 20), borderwidth=2, relief="groove", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)  # Botón limpiar
        ]

        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 14, "bold"),
                                bg="#00b894", fg="white", command=self.calculate)
            elif text == 'C':
                btn = tk.Button(master, text=text, width=23, height=2, font=("Arial", 14, "bold"),
                                bg="#d63031", fg="white", command=self.clear)
                btn.grid(row=row, column=col, columnspan=4, padx=5, pady=5)
                continue
            else:
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 14),
                                command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'x':
            self.expression += '*'
        elif char == '÷':
            self.expression += '/'
        else:
            self.expression += char
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
            self.expression = result
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
