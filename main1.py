import tkinter as tk
from tkinter import messagebox


# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


# Creating the main application window
app = tk.Tk()
app.title("Calculator")

# Entry fields for numbers
tk.Label(app, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(app)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(app)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Radio buttons for operation selection
operation_var = tk.StringVar(value="+")
tk.Label(app, text="Choose an operation:").grid(row=2, column=0, padx=10, pady=10)

tk.Radiobutton(app, text="Addition (+)", variable=operation_var, value="+").grid(row=2, column=1)
tk.Radiobutton(app, text="Subtraction (-)", variable=operation_var, value="-").grid(row=3, column=1)
tk.Radiobutton(app, text="Multiplication (*)", variable=operation_var, value="*").grid(row=4, column=1)
tk.Radiobutton(app, text="Division (/)", variable=operation_var, value="/").grid(row=5, column=1)

# Button to perform calculation
calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(app, text="Result: ")
result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Run the application
app.mainloop()
