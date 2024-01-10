import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_var = tk.IntVar(value=12)
        self.include_letters_var = tk.BooleanVar(value=True)
        self.include_numbers_var = tk.BooleanVar(value=True)
        self.include_symbols_var = tk.BooleanVar(value=True)

        self.create_gui()

    def generate_password(self):
        length = self.length_var.get()
        include_letters = self.include_letters_var.get()
        include_numbers = self.include_numbers_var.get()
        include_symbols = self.include_symbols_var.get()

        if not (include_letters or include_numbers or include_symbols):
            messagebox.showerror("Error", "Select at least one character type.")
            return

        all_characters = ""
        if include_letters:
            all_characters += string.ascii_letters
        if include_numbers:
            all_characters += string.digits
        if include_symbols:
            all_characters += string.punctuation

        generated_password = ''.join(random.choice(all_characters) for _ in range(length))
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, generated_password)

    def copy_to_clipboard(self):
        password = self.result_entry.get()
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")

    def create_gui(self):
        frame = ttk.Frame(self.root, padding="20")
        frame.grid(row=0, column=0, sticky="wens")  # Fix: use "wens" instead of (tk.W, tk.E, tk.N, tk.S)

        ttk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky=tk.W)
        length_entry = ttk.Entry(frame, textvariable=self.length_var, width=5)
        length_entry.grid(row=0, column=1, sticky=tk.W)

        ttk.Checkbutton(frame, text="Include Letters", variable=self.include_letters_var).grid(row=1, column=0, sticky=tk.W)
        ttk.Checkbutton(frame, text="Include Numbers", variable=self.include_numbers_var).grid(row=2, column=0, sticky=tk.W)
        ttk.Checkbutton(frame, text="Include Symbols", variable=self.include_symbols_var).grid(row=3, column=0, sticky=tk.W)

        generate_button = ttk.Button(frame, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

        self.result_entry = ttk.Entry(frame, width=30)
        self.result_entry.grid(row=5, column=0, columnspan=2, pady=(10, 0))

        copy_button = ttk.Button(frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=6, column=0, columnspan=2, pady=(10, 0))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
