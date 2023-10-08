import tkinter as tk
import random
import string
from tkinter import messagebox

# Function to generate a random password with animation
def generate_password_with_animation():
    length = int(length_entry.get())
    if length < 8:
        messagebox.showerror("Error", "Password length must be at least 8 characters")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(length))
        animate_password(generated_password)

# Function to animate the generated password
def animate_password(password):
    if password:
        result_label.config(text="Generated Password: " + password[0])
        root.after(100, lambda: animate_password(password[1:]))
    else:
        result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate password with animation
generate_button = tk.Button(root, text="Generate Password with Animation", command=generate_password_with_animation)
generate_button.pack()

# Label to display generated password
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI main loop
root.mainloop()
