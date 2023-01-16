import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("200x250")

        self.result = tk.Entry(self, width=35, borderwidth=5)
        self.result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_button("1", 1, 1)
        self.create_button("2", 1, 2)
        self.create_button("3", 1, 3)

        self.create_button("4", 2, 1)
        self.create_button("5", 2, 2)
        self.create_button("6", 2, 3)

        self.create_button("7", 3, 1)
        self.create_button("8", 3, 2)
        self.create_button("9", 3, 3)

        self.create_button(".", 4, 1)
        self.create_button("0", 4, 2)
        self.create_button("C", 4, 3)

        self.create_button("+", 5, 1)
        self.create_button("-", 5, 2)
        self.create_button("*", 5, 3)
        self.create_button("/", 6, 1)
        self.create_button("=", 6, 2)
        self.create_button("%", 6, 3)

    def create_button(self, text, row, column):
        button = tk.Button(self, text=text, padx=40, pady=20, command=lambda: self.button_click(text))
        button.grid(row=row, column=column)

    def button_click(self, text):
        if text == "C":
            self.result.delete(0, tk.END)
        elif text in "+-*/%":
            current = self.result.get()
            if current and current[-1] in "+-*/%":
                current = current[:-1]
            self.result.delete(0, tk.END)
            self.result.insert(0, current + text)
        elif text == "=":
            try:
                current = self.result.get()
                if current[0] == "-":
                    current = "0" + current
                self.result.delete(0, tk.END)
                self.result.insert(0, eval(current))
            except:
                self.result.delete(0, tk.END)
                self.result.insert(0, "Error")
        else:
            current = self.result.get()
            self.result.delete(0, tk.END)
            self.result.insert(0, current + text)


calc = Calculator()
calc.mainloop()
