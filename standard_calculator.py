# Standard Calculator: operates like a simple non-scientific desktop calculator

import tkinter as tk
from tkinter import *

# Window setup
root = tk.Tk()
root.geometry("230x280")
root.title("CalcBox")
root.config(bg="dark gray")

parent_frame = tk.Frame(root, bd=5, relief=SUNKEN, bg="gray")
parent_frame.pack(fill="both", expand=TRUE)
calc_frame = tk.Frame(parent_frame, bd=5, bg="gray")
calc_frame.pack(expand=TRUE)

# Entry field
entry = tk.Entry(calc_frame, width=20, font=("Arial", 8))
entry.pack()

button_frame = tk.Frame(calc_frame, bd=5, relief=tk.SUNKEN, bg="gray")
button_frame.pack(expand=True, padx=15, pady=15)

# Functions
def button_click(value):
    # Inserts number input with appending instead of replacing
    entry.insert(tk.END, value)

def clear_entry():
    # Clears entry
    entry.delete(0, tk.END)

def delete_last():
    # Deleted the last character from input
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate_result():
    # Evaluates input expression and prints the results
    try:
        expression = entry.get().replace("x", "*")  # Replaces x with * for multiplication
        result = eval(expression)  # Simple evaluation function
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Syntax Error")

def calculate_percentage():
    # Provides function to % button that turns number into percent
    try:
        current_value = entry.get()
        if current_value:
            percent_value = float(current_value) / 100
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(percent_value))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Syntax Error")


''' Button Grid Setup: .grid() allows much cleaner placement of elements and gives the main calculator look
      |columns|
|rows| 0 1 2 3            
       1 1
       2   2
       3     3 
       4   2
       5 1     '''

# Buttons -> lambda is used for command to assign used functions anonymously
percent = tk.Button(button_frame, text="%", command=calculate_percentage)
percent.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)  # nsew makes button expand to fill in all 4 directions

recip = tk.Button(button_frame, text="1/x", command=lambda: button_click("**-1"))
recip.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

seven = tk.Button(button_frame, text="7", command=lambda: button_click("7"))
seven.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

four = tk.Button(button_frame, text="4", command=lambda: button_click("4"))
four.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

one = tk.Button(button_frame, text="1", command=lambda: button_click("1"))
one.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

sign = tk.Button(button_frame, text="+/-", command=lambda: button_click("-"))
sign.grid(row=5, column=0, sticky="nsew", padx=2, pady=2)

clear_e = tk.Button(button_frame, text="CE", command=clear_entry)  # Clears input
clear_e.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)

expo = tk.Button(button_frame, text="x²", command=lambda: button_click("**2"))
expo.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)

eight = tk.Button(button_frame, text="8", command=lambda: button_click("8"))
eight.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)

five = tk.Button(button_frame, text="5", command=lambda: button_click("5"))
five.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)

two = tk.Button(button_frame, text="2", command=lambda: button_click("2"))
two.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)

zero = tk.Button(button_frame, text="0", command=lambda: button_click("0"))
zero.grid(row=5, column=1, sticky="nsew", padx=2, pady=2)

clear = tk.Button(button_frame, text="C", command=clear_entry)  # Also clears input
clear.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)

sqrt = tk.Button(button_frame, text="√", command=lambda: button_click("**0.5"))
sqrt.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

nine = tk.Button(button_frame, text="9", command=lambda: button_click("9"))
nine.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)

six = tk.Button(button_frame, text="6", command=lambda: button_click("6"))
six.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)

three = tk.Button(button_frame, text="3", command=lambda: button_click("3"))
three.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)

decimal = tk.Button(button_frame, text=".", command=lambda: button_click("."))
decimal.grid(row=5, column=2, sticky="nsew", padx=2, pady=2)

delete = tk.Button(button_frame, text="⌫", command=delete_last)  # Only clears last integer
delete.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)

divide = tk.Button(button_frame, text="/", command=lambda: button_click("/"))
divide.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)

multiply = tk.Button(button_frame, text="x", command=lambda: button_click("*"))
multiply.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)

sub = tk.Button(button_frame, text="-", command=lambda: button_click("-"))
sub.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)

add = tk.Button(button_frame, text="+", command=lambda: button_click("+"))
add.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

equal = tk.Button(button_frame, text="=", command=calculate_result)  # Performs evaluation function for result
equal.grid(row=5, column=3, sticky="nsew", padx=2, pady=2)

root.mainloop()
