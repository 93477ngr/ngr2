import tkinter as tk
from tkinter import messagebox

# Function to update the expression in the input field
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except ZeroDivisionError:
        equation.set("Error")
        expression = ""
    except:
        equation.set("Error")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    equation.set("")

# Main GUI setup
if __name__ == "__main__":
    # Creating main window
    root = tk.Tk()
    root.title("Modern Calculator")
    root.configure(background="lightgray")
    root.geometry("400x500")
    
    # Global variable for expression
    expression = ""

    # StringVar to update the input field
    equation = tk.StringVar()

    # Input field
    input_field = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4, bg="powder blue")
    input_field.grid(columnspan=4, ipadx=8)

    # Buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ]

    for (text, row, col) in buttons:
        if text == '=':
            button = tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="black", bg="light green",
                               font=('Arial', 18), command=equalpress)
        else:
            button = tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="black", bg="light yellow",
                               font=('Arial', 18), command=lambda t=text: press(t))
        button.grid(row=row, column=col)

    clear_button = tk.Button(root, text="C", padx=20, pady=20, bd=8, fg="black", bg="light coral",
                             font=('Arial', 18), command=clear)
    clear_button.grid(row=5, column=0, columnspan=4)

    # Start the GUI event loop
    root.mainloop()
