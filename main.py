import tkinter as tk
import random
import string

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

    def create_widgets(self):
        label = tk.Label()

    def generate_password(self):
        length = self.length_var.get()


if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()