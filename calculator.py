import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Create entry field
        self.result_var = tk.StringVar()
        self.entry = ttk.Entry(root, textvariable=self.result_var, justify="right", font=('Arial', 20))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Create buttons
        self.create_buttons()

        # Configure grid
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        button_data = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0, 2)  # Clear button spans 2 columns
        ]

        for button in button_data:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = button[3] if len(button) > 3 else 1

            btn = ttk.Button(
                self.root,
                text=text,
                command=lambda t=text: self.button_click(t)
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")

    def button_click(self, value):
        current = self.result_var.get()

        if value == 'C':
            self.result_var.set('')
        elif value == '=':
            try:
                result = eval(current)
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.result_var.set('')
        else:
            self.result_var.set(current + value)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 