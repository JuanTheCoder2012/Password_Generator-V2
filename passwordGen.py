import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    if length < 8:
        messagebox.showerror("Error", "Password length must be at least 8 characters")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display generated password
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI main loop
root.mainloop()
