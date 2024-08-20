# todo_gui.py

import tkinter as tk
from tkinter import messagebox

# Main application class
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TO-DO LIST")

        # Task list
        self.tasks = []

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Task entry
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add task button
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10, pady=10)

        # Task listbox
        self.tasks_listbox = tk.Listbox(self.root, width=50, height=20)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Mark as completed button
        self.complete_task_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_task_completed)
        self.complete_task_button.grid(row=2, column=0, padx=10, pady=10)

        # Delete task button
        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task_title = self.task_entry.get()
        if task_title:
            self.tasks.append({"title": task_title, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task_list(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["completed"] else "Pending"
            self.tasks_listbox.insert(tk.END, f'{task["title"]} [{status}]')

    def mark_task_completed(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            selected_task = self.tasks[selected_task_index[0]]
            selected_task["completed"] = True
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select atleast one task to delete.")

# Main function to run the application
def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


