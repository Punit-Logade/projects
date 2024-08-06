import subprocess
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import csv
from PIL import Image, ImageTk
import hashlib

USER_CSV_FILE = "user_data.csv"

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def read_users_from_csv():
    users = {}
    try:
        with open(USER_CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    users[row[0]] = row[1]  
    except FileNotFoundError:
        pass
    return users

def write_user_to_csv(username, hashed_password):
    with open(USER_CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password])

def register_user(username, password):
    hashed_password = hash_password(password)
    users = read_users_from_csv()
    if username in users:
        return "Username already exists."
    write_user_to_csv(username, hashed_password)
    return "User registered successfully."
    return True

def login_user(username, password):
    hashed_password = hash_password(password)
    users = read_users_from_csv()
    if users.get(username) == hashed_password:
        return True
    return False

# Creating the login window
window = ttk.Window(themename='superhero')
window.title('Login Page')

# Create frame for layout
frame = ttk.Frame(window)
frame.pack(expand=True, fill='both')

# Load and set the background image
# image_path = r'C:\Users\punit\OneDrive\Desktop\apps\projects\task_manneger_materials\image_1.jpg'
# back_image = Image.open(image_path)
# background_image = ImageTk.PhotoImage(back_image)
# back_label = ttk.Label(window, image=background_image)
# back_label.place(relwidth=1, relheight=1)

# Define login function
def login():
    username = username_entry.get()
    password = password_entry.get()
    if login_user(username, password):
        messagebox.showinfo("Login Successful", "Login successful.")
        window.destroy()
        script_path = r'C:\Users\punit\OneDrive\Desktop\apps\projects\task_manneger_materials\GUI_1.py'
        subprocess.run(["python", script_path])
    else:
        messagebox.showerror("Login Error", "Login failed. Check your username and password.")
#new user
def new_user():
    username = username_entry.get()
    password = password_entry.get()
    if register_user(username, password):
        messagebox.showinfo("Registration Successfull", "Registration Successfull \nyou can Login Now")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    else:
        messagebox.showerror("Registration Failed", "Registration Failed. Username already exists.")

# Create and place widgets
tk.Label(frame, text="Username:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(frame, text="Password:").grid(row=1, column=0, padx=10, pady=10)

username_entry = tk.Entry(frame)
password_entry = tk.Entry(frame, show="*")

username_entry.grid(row=0, column=1, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(frame, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(frame, text= 'Registr', command=new_user).grid(row=3, column=0, columnspan=2, pady=20)

window.mainloop()