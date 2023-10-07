import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password and animate it
def generate_and_animate_password():
    length = int(length_entry.get())
    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
    else:
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_characters) for _ in range(length))
        animate_password(password, 0)

# Function to animate the password letter by letter
def animate_password(password, index):
    if index < len(password):
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, password[:index+1])
        index += 1
        password_entry.after(100, animate_password, password, index)

# GUI setup
root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root, width=20)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_animate_password)
generate_button.pack()

password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack()

root.mainloop()

