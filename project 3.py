import tkinter as tk
from tkinter import ttk , messagebox, simpledialog
import ttkbootstrap as ttk
# Creating a window with addition project runing options
window_1 = ttk.Window(themename ="journal")
window_1.title('Project selection')
window_1.geometry('500x500')

# Adding Wideges
lable1 = ttk.Label(master= window_1, text = 'Please choose the project', font= ('Roboto', 12) ,)
lable1.pack()
# EXIT FUNCTION
def exit():
    window_1.destroy()

# projects
# Km to miles Converter
def kilometer_func():
    # km to mile converter 
    root1 = ttk.Window(themename= 'vapor')
    root1.geometry('350x250')
    lable = ttk.Label(root1, text='Km to miles Converter')
    lable.pack()
    # Function to convert km to miles
    def convert():
        try:
            km = float(entry.get())
            miles = km * 0.621371
            result.config(text=f'{km} km is equal to {miles:.2f} miles')
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid number')

    # Making wideges

    frame = ttk.Frame(master= root1)
    frame.pack()
    entry = ttk.Entry(frame)
    entry.pack(side='left', padx=10)
    button = ttk.Button(frame, command=convert, text='Convert' )
    button.pack(side='right')
    result = ttk.Label(root1)
    result.pack()

    root1.mainloop()

# ATM
def atm():
    import tkinter as tk

    from tkinter import messagebox, simpledialog

    balance = 100000
    pin = 1234

    root = tk.Tk()
    root.geometry("500x500")
    lable = tk.Label(root, text = 'Welcome To ATM !!')
    root.configure( bg='blue')
    root.title('ATM Menu')

    #creating a message box for pin

    def pin_func():
        m1 = simpledialog.askinteger("Please Enter Your pin", "Please Enter your Pin :")
        global pin
        try: 
            m = int(m1)

            try:
                m1 == pin 
                return True
            except:
                messagebox.showwarning("Error","Please Enter correct pin ")
                return False
        except:
            messagebox.showerror("valuerror", "Please enter valid pin number (numbers only)")
            return False

    #creating a messagebox for balance inquiry

    def balance_func():
        try:
            pin_func()
            messagebox.showinfo("Info box", " your current balance is %s" % balance)
        except:
            messagebox.showwarning("warning", "please Enter Corrct pin")
    #creating a messagebox for withdraw

    def withdraw_func():
        global balance
        w = simpledialog.askinteger("Info box", " Enter withdraw Amount.")
        try:
            pin_func()
        
            if w is not None :
                w1 = int(w)
                try:
                    w1<=balance
                    balance -= w1
                    messagebox.showinfo("Info box", " Tranjection successfull.       please collect the money " )
                except :
                    messagebox.showerror("Error","withrowal amount exceeds your current balance")
            else :
                messagebox.showinfo("Info box", "please enter valid input")  
        except ValueError:
            messagebox.showerror("Error","Please input valid info")

    def deposit_func():
        global balance
        b = simpledialog.askinteger("Info box", "Enter Deposite Amount" ) 
        try:
            pin_func()
            if b is not None:
                b1 = int(b)
                try:
                    balance += int(b1)
                    messagebox.showinfo("Info Box","Tranjection successfull")
                except :
                    messagebox.showerror("Error","Enter the valid input")
            else :
                messagebox.showinfo("Info box", "please enter valid input")  
        except ValueError:
            messagebox.showerror("Error","Please input valid input")

    #Change pin function 

    def change_pin_func():
        global pin
        try:
            pin_func()
            new_pin = simpledialog.askinteger("Please Enter Your New Pin", "Please Enter your New Pin :")
        except:
            messagebox.showwarning("Error","Please enter Valid PIN")       

    # exit function

    def exit_func():
        root.destroy()



    # Interface
    # welcome message


    l = tk.Label(root, text="Welome to the SBI ATM.", bg= "blue", fg= "black", font= ("Helvetica", 20), justify=tk.CENTER)


    l1 = tk.Label(root, text="please Choose an option.", bg= "blue", fg= "black", font= ("Helvetica", 10), justify=tk.CENTER)
    l.pack(pady=20)
    l1.pack(pady=10)

    #creating button frame
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True) 

    #Creating the buttons

    b0 = tk.Button(button_frame, text="Balance inquiry", bg= "black", fg= "#FF00FF", font= ("Helvetica", 16) , justify= tk.LEFT, command= balance_func)
    b0.grid(row= 1, column = 2,pady=10)

    b1 = tk.Button(button_frame, text="Withdraw        ", bg= "black", fg= "#FF00FF", font= ("Helvetica", 16) , justify= tk.LEFT, command= withdraw_func)
    b1.grid(row= 2, column = 2,pady=10)

    b2 = tk.Button(button_frame, text="Deposite        ", bg= "black", fg= "#FF00FF", font= ("Helvetica", 16) , justify= tk.LEFT,
    command=deposit_func)
    b2.grid(row= 3, column = 2,pady=10)

    b3 = tk.Button(button_frame, text="Change Pin      ", bg= "black", fg= "#FF00FF", font= ("Helvetica", 16) , justify= tk.LEFT, command= change_pin_func)
    b3.grid(row= 4, column = 2,pady=10)

    b4 = tk.Button(button_frame, text="EXIT              ", bg= "black", fg= "#FF00FF", font= ("Helvetica", 16) , justify= tk.LEFT, command=exit_func)
    b4.grid(row= 5, column = 2, pady=10)
    root.mainloop()

# Finance app

def finance():
    #making a income and expence program

    income_list = []
    expence_list = []

    # income function
    def income_fun():
        global income_list
        desc = income_desc.get()     # income descriptor
        amount = income_amount.get()  # income amount
        if desc and amount:
            income_list.append((desc, amount))
            messagebox.showinfo("Success", "Income added successfully!")
            income_desc_entry.delete(0, tk.END)
            income_amount_entry.delete(0, tk.END)

        else:
            messagebox.showwarning("Error", "Please enter a description and amount")        
        
    # Expence function

    def expense_fun():
        global expence_list
        desc = expense_desc.get()     # expense descriptor
        amount = expense_amount.get()  # expense amount
        if desc and amount:
            expence_list.append((desc, amount))
            messagebox.showinfo("Success", "Expense added successfully!")
            expense_desc_entry.delete(0, tk.END)
            expense_amount_entry.delete(0, tk.END)

    # sumary fnction

    def summary_fun():
        global expence_list
        total_income = sum(amount for _ , amount in  income_list) 
        total_expense = sum(amount for _ , amount in expence_list)
        total_balance = total_income - total_expense

        summary = f"Total Income: ${total_income}\nTotal Expence: ${total_expense} Total Balance: ${total_balance}\n\n"     

        summary += "\nExpense Entries:\n"
        for desc, amount in expense_list :
            summary += f"{desc}: ${amount}\n"

        summary_text.config(state='normal')
        summary_text.delete(1.0, tk.END)
        summary_text.insert(tk.END, summary)
        summary_text.config(state='disabled')


    root = tk.Tk()
    root.title("Personal Finance Tracker")
    root.geometry("500x400")

    # Income Frame
    income_frame = ttk.LabelFrame(root, text="Add Income")
    income_frame.pack(fill="x", padx=10, pady=5)

    income_desc = tk.StringVar()
    income_amount = tk.DoubleVar()

    tk.Label(income_frame, text="Description").grid(row=0, column=0, padx=5, pady=5)
    income_desc_entry = tk.Entry(income_frame, textvariable=income_desc)
    income_desc_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(income_frame, text="Amount").grid(row=1, column=0, padx=5, pady=5)
    income_amount_entry = tk.Entry(income_frame, textvariable=income_amount)
    income_amount_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(income_frame, text="Add Income", command=income_fun).grid(row=2, columnspan=2, pady=5)

    # Expense Frame
    expense_frame = ttk.LabelFrame(root, text="Add Expense")
    expense_frame.pack(fill="x", padx=10, pady=5)

    expense_desc = tk.StringVar()
    expense_amount = tk.DoubleVar()

    tk.Label(expense_frame, text="Description").grid(row=0, column=0, padx=5, pady=5)
    expense_desc_entry = tk.Entry(expense_frame, textvariable=expense_desc)
    expense_desc_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(expense_frame, text="Amount").grid(row=1, column=0, padx=5, pady=5)
    expense_amount_entry = tk.Entry(expense_frame, textvariable=expense_amount)
    expense_amount_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(expense_frame, text="Add Expense", command=expense_fun).grid(row=2, columnspan=2, pady=5)

    # Summary Frame
    summary_frame = ttk.LabelFrame(root, text="Summary")
    summary_frame.pack(fill="both", expand=True, padx=10, pady=5)

    tk.Button(summary_frame, text="View Summary", command=summary_fun).pack(pady=10)

    summary_text = tk.Text(summary_frame, height=10, state='disabled')
    summary_text.pack(fill="both", padx=10, pady=5)

    root.mainloop()
    
   #

# Calculator

def Calculator():
    #Calculator
    # Making a window
    root = ttk.Window(themename= 'journal')
    root.title('Calculator')
    root.geometry('500x400')
    # Adding label
    intvar= tk.IntVar()
    label= ttk.Label(master= root, text='0', textvariable= intvar)
    label.grid(row=0,column=3 ,columnspan= 3,pady=5, padx=5 )


    def click_event(key):
        global expression
        if key == "=":
            try:
                expression = expression.replace('^', '**')
                expression = expression.replace('pi', str(math.pi))
                expression = expression.replace('sqrt', 'math.sqrt')
                expression = expression.replace('log', 'math.log10')
                expression = expression.replace('ln', 'math.log')
                expression = expression.replace('exp', 'math.exp')
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('deg', 'math.degrees')
                expression = expression.replace('rad', 'math.radians')

                result = str(eval(expression))
                display.delete(0, tk.END)
                display.insert(tk.END, result)
                expression = ""
            except Exception as e:
                display.delete(0, tk.END)
                display.insert(tk.END, "Error")
                expression = ""
        elif key == "C":
            expression = ""
            display.delete(0, tk.END)
        else:
            expression += str(key)
            display.delete(0, tk.END)
            display.insert(tk.END, expression)


    # Dispay

    display = ttk.Entry(root, font=("Arial", 20), justify="right", background="#ffffff", textvariable=intvar)
    display.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=10, padx=10, pady=20)

    #button 
    button_list = [
        '7', '8', '9', '/', 'C',
        '4', '5', '6', '*', 'sqrt',
        '1', '2', '3', '-', 'log',
        '0', '.', '+', '=', 'pi',
        'sin', 'cos', 'tan', '(', ')',
        'exp', 'ln', 'deg', 'rad', '^'
        ]

    row = 1
    col= 0    
    for button in button_list:
        action = lambda x=button: click_event(x)
        ttk.Button(root, text=button, command=action, width=10).grid(row=row, column=col, pady=5, padx=5)
        col += 1
        if col > 4:
            col = 0
            row += 1




    #Run
    root.mainloop()



# Buttons
button_frame= ttk.Frame(master= window_1)

button1 = ttk.Button(master= button_frame, text = 'Km to miles Converter' , command=kilometer_func)
button2 = ttk.Button(master= button_frame, text = 'ATM Machine          ' , command=atm)
button3 = ttk.Button(master= button_frame, text = '       EXIT              ' , command=exit )
button4 = ttk.Button(master= button_frame, text = 'Personal Finance App ' , command=finance )
button5 = ttk.Button(master= button_frame, text = 'Calculator ' , command=Calculator )

# Run
button_frame.pack()
button1.grid(row=1, column=1, padx=15, pady=5)
button2.grid(row=1, column=2, padx=15, pady=5)
button3.grid(row=2, column=1, padx=15, pady=5)
button4.grid(row=2, column=2, padx=15, pady=5)
button5.grid(row=3, column=1, padx=15, pady=5) 

window_1.mainloop()