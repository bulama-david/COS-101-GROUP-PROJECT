import tkinter as tk
import random
import string

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Password Generator")
        self.geometry("400x400")

        self.create_widgets()


    def create_widgets(self):
        label = tk.Label()

    def generate_password(self):
        length = self.length_var.get()


if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
