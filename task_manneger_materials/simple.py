import tkinter
from tkinter import* 
i = 0
tasks = []
# making a task list
def tasklist():
    n = input('Enter the new Task . ')
    tasks.append([n])
    print('Task added successfully!')

def task_update():
    index = int(input('Enter the index of the task to update. '))
    new_task = input('Enter the new task. ')
    tasks[index-1][0] = new_task
    print('Task updated successfully!')

def delete_task():
        index = int(input('Enter the index of the task to delete. '))
        del tasks[index-1]
        print('Task deleted successfully!')
def summary_task():
    print('Task Summary:')
    for i, task in enumerate(tasks, start=1):
        print(f'{i}. {task[0]}')
def exit ():
    return i==1
# Main menu
while True:
    print(' Choose a funtion')           
    print('1.Add a New task')
    print('2.Update the task')
    print('3.Delete a task')
    print('4.see Task Summary')
    print('5.EXIT')
    choice = int(input('Enter your choice: '))
    if choice ==1:
        tasklist()
    elif choice ==2:
        task_update()
    elif choice ==3:
        delete_task()    
    elif choice ==4:
        summary_task()
    elif choice ==5:
        exit ()  
    else :
        print('Invalid choice! Try again.')
