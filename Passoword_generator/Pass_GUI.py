import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_entry.get()
    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Error", "Please enter a valid positive integer for password length.")
        return
    
    length = int(length)
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    
    if not (use_letters or use_numbers or use_symbols):
        messagebox.showerror("Error", "Please select at least one character type.")
        return
    
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Create main window
window = tk.Tk()
window.title("Password Generator")

# Create widgets
length_label = tk.Label(window, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=5, pady=5)

letters_var = tk.BooleanVar()
letters_var.set(True)
letters_check = tk.Checkbutton(window, text="Include Letters", variable=letters_var)
letters_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")

numbers_var = tk.BooleanVar()
numbers_var.set(True)
numbers_check = tk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
numbers_check.grid(row=2, column=0, padx=5, pady=5, sticky="w")

symbols_var = tk.BooleanVar()
symbols_var.set(True)
symbols_check = tk.Checkbutton(window, text="Include Symbols", variable=symbols_var)
symbols_check.grid(row=3, column=0, padx=5, pady=5, sticky="w")

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

password_label = tk.Label(window, text="Generated Password:")
password_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI
window.mainloop()
