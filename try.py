import tkinter as tk
from tkinter import messagebox, simpledialog
import ttkbootstrap as ttk
import csv
import hashlib

# File paths
USER_CSV_FILE = "user_data.csv"
TASK_CSV_FILE = "tasks.csv"

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

def login_user(username, password):
    hashed_password = hash_password(password)
    users = read_users_from_csv()
    if users.get(username) == hashed_password:
        return True
    return False

# Task manager functions
def read_tasks_from_csv():
    tasks = []
    try:
        with open(TASK_CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            tasks = [row for row in reader]
    except FileNotFoundError:
        pass
    return tasks

def write_tasks_to_csv(tasks):
    with open(TASK_CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

def show_login_page():
    print("Displaying login page...")
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Username:").grid(row=0, column=0)
    tk.Label(root, text="Password:").grid(row=1, column=0)

    username_entry = tk.Entry(root)
    password_entry = tk.Entry(root, show="*")

    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if login_user(username, password):
            show_task_manager()
        else:
            messagebox.showerror("Login Error", "Login failed. Check your username and password.")

    tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2)

def show_task_manager():
    print("Displaying task manager...")
    for widget in root.winfo_children():
        widget.destroy()

    global tasklist
    tasklist = read_tasks_from_csv()

    root.title("Task Manager")

    btn_frame = ttk.Frame(root)
    btn_frame.grid(row=0, column=0, columnspan=2)

    main_frame = tk.Frame(root, background="#66FF66")
    main_frame.grid(row=0, column=3, columnspan=4)

    label_1 = ttk.Label(main_frame, text="Task Manager", font=('lobster', 25))
    label_1.pack(pady=50, padx=20)

    tasklist_frame = ttk.Frame(main_frame)
    tasklist_frame.pack(padx=20, pady=20)

    def refresh_tasklist():
        for widget in tasklist_frame.winfo_children():
            widget.destroy()
        for i, task in enumerate(tasklist, start=1):
            task_label = ttk.Label(tasklist_frame, text=f"{i}. {task[0]}")
            task_label.pack(anchor='w')

    def open_add_task_window():
        sub_window = tk.Toplevel(root)
        sub_window.title("Add Task")
        
        sub_label = ttk.Label(sub_window, text="Enter a New Task")
        sub_label.pack(padx=20, pady=20)
        
        sub_entry = ttk.Entry(sub_window)
        sub_entry.pack(padx=20, pady=20)
        
        def submit():
            task = sub_entry.get()
            if not task:
                messagebox.showerror(master=sub_window, message='Invalid input. Please enter a valid task.')
            else:
                tasklist.append([task, ''])
                write_tasks_to_csv(tasklist)
                refresh_tasklist()
                messagebox.showinfo(master=sub_window, title="Info", message='Task added successfully!')
                sub_window.destroy()
        
        submit_btn = ttk.Button(sub_window, text='Submit', command=submit)
        submit_btn.pack(padx=10, pady=10)
        
        sub_window.transient(root)
        sub_window.grab_set()
        root.wait_window(sub_window)

    def open_update_task_window():
        sub_window = tk.Toplevel(root)
        sub_window.title("Update Task")
        
        sub_label = ttk.Label(sub_window, text="Enter the index of the task to update")
        sub_label.pack(padx=20, pady=20)
        
        sub_entry = ttk.Entry(sub_window)
        sub_entry.pack(padx=20, pady=20)
        
        def submit_index():
            try:
                index = int(sub_entry.get())
                if 1 <= index <= len(tasklist):
                    sub_label.config(text='Enter the new task')
                    sub_entry.delete(0, tk.END)
                    
                    def submit_task():
                        new_task = sub_entry.get()
                        if new_task:
                            tasklist[index - 1][0] = new_task
                            write_tasks_to_csv(tasklist)
                            refresh_tasklist()
                            messagebox.showinfo(master=sub_window, title="Task Update", message='Task updated successfully!')
                            sub_window.destroy()
                        else:
                            messagebox.showerror(master=sub_window, message='Invalid input. Please enter a valid task.')
                    
                    submit_task_btn = ttk.Button(sub_window, text='Submit', command=submit_task)
                    submit_task_btn.pack(padx=10, pady=10)
                    
                else:
                    messagebox.showerror(master=sub_window, message='Invalid index. Please enter a valid index.')
                    sub_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror(master=sub_window, message='Invalid input. Please enter a valid number.')
                sub_entry.delete(0, tk.END)
        
        submit_index_btn = ttk.Button(sub_window, text='Submit', command=submit_index)
        submit_index_btn.pack(padx=10, pady=10)
        
        sub_window.transient(root)
        sub_window.grab_set()
        root.wait_window(sub_window)

    def open_delete_task_window():
        sub_window = tk.Toplevel(root)
        sub_window.title("Delete Task")
        
        sub_label = ttk.Label(sub_window, text="Enter the index of the task to delete")
        sub_label.pack(padx=20, pady=20)
        
        sub_entry = ttk.Entry(sub_window)
        sub_entry.pack(padx=20, pady=20)
        
        def submit():
            try:
                index = int(sub_entry.get())
                if 1 <= index <= len(tasklist):
                    ans = simpledialog.askstring('Confirmation', f'Do you want to delete task at index {index} (yes / no)?')
                    if ans == 'yes':
                        tasklist.pop(index - 1)
                        write_tasks_to_csv(tasklist)
                        refresh_tasklist()
                        messagebox.showinfo(master=sub_window, title="Task Delete", message='Task deleted successfully!')
                        sub_window.destroy()
                    else:
                        sub_entry.delete(0, tk.END)
                else:
                    messagebox.showerror(master=sub_window, message='Invalid index. Please enter a valid index.')
                    sub_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror(master=sub_window, message='Invalid input. Please enter a valid number.')
                sub_entry.delete(0, tk.END)
        
        submit_btn = ttk.Button(sub_window, text='Delete', command=submit)
        submit_btn.pack(padx=10, pady=10)
        
        sub_window.transient(root)
        sub_window.grab_set()
        root.wait_window(sub_window)

    def exit_app():
        messagebox.showinfo(master=root, title="Exit", message='Thank you for using this Task Manager')
        root.destroy()

    btn_1 = ttk.Button(btn_frame, text='Add a Task', command=open_add_task_window)
    btn_2 = ttk.Button(btn_frame, text='Update a Task', command=open_update_task_window)
    btn_3 = ttk.Button(btn_frame, text='Delete a Task', command=open_delete_task_window)
    btn_4 = ttk.Button(btn_frame, text='EXIT', command=exit_app)

    btn_1.pack(padx=10, pady=10)
    btn_2.pack(padx=10, pady=10)
    btn_3.pack(padx=10, pady=10)
    btn_4.pack(padx=10, pady=10)

    refresh_tasklist()
    root.mainloop()

if __name__ == "__main__":
    print("Starting the application...")
    root = tk.Tk()
    root.withdraw()
    show_login_page()
    root.mainloop()
