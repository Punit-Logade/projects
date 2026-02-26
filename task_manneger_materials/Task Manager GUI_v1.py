import tkinter as tk
from tkinter import simpledialog, messagebox
import ttkbootstrap as ttk
import csv

# File to store tasks
CSV_FILE = 'tasks.csv'

# Function to read all tasks from the CSV file
def read_tasks_from_csv():
    tasks = []
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            tasks = [row for row in reader]
    except FileNotFoundError:
        pass
    return tasks

# Function to write all tasks to the CSV file
def write_tasks_to_csv(tasks):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

# Initialize task list from CSV
tasklist = read_tasks_from_csv()

# Creating a root window
root = ttk.Window(themename='vapor')
root.title("Task Manager")

# Creating a frame
btn_frame = ttk.Frame(root)
btn_frame.grid(row=0, column=0, columnspan=2)

main_frame = tk.Frame(root, background="#66FF66")
main_frame.grid(row=0, column=3, columnspan=4)

# Placing main frame widgets
label_1 = ttk.Label(main_frame, text="Task Manager", font=('lobster', 25))
label_1.pack(pady=50, padx=20)

label = ttk.Label(main_frame, text="")
label.pack(padx=20)

tasklist_frame = ttk.Frame(main_frame)
tasklist_frame.pack(padx=20, pady=20)

# Function to refresh the task list display
def refresh_tasklist():
    for widget in tasklist_frame.winfo_children():
        widget.destroy()
    for i, task in enumerate(tasklist, start=1):
        task_label = ttk.Label(tasklist_frame, text=f"{i}. {task[0]}")
        task_label.pack(anchor='w')

# Function to open a sub-window for adding a new task
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

# Function to open a sub-window for updating a task
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
    
    submit_index_btn = ttk.Button(sub_window, text='Submit', command=lambda:[submit_index(), submit_index_btn.destroy()])
    submit_index_btn.pack(padx=10, pady=10)
    
    
    sub_window.transient(root)
    sub_window.grab_set()
    root.wait_window(sub_window)

# Function to open a sub-window for deleting a task
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

# Function to exit the application
def exit_app():
    messagebox.showinfo(master=root, title="Exit", message='Thank you for using this Task Manager')
    root.destroy()

# Creating buttons
btn_1 = ttk.Button(btn_frame, text='Add a Task', command=open_add_task_window)
btn_2 = ttk.Button(btn_frame, text='Update a Task', command=open_update_task_window)
btn_3 = ttk.Button(btn_frame, text='Delete a Task', command=open_delete_task_window)
btn_4 = ttk.Button(btn_frame, text='EXIT', command=exit_app)

btn_1.pack(padx=10, pady=10)
btn_2.pack(padx=10, pady=10)
btn_3.pack(padx=10, pady=10)
btn_4.pack(padx=10, pady=10)

# Initial task list refresh
refresh_tasklist()

root.mainloop()
