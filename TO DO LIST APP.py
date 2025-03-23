import tkinter as tk
from tkinter import messagebox, ttk
import os

# Define the functions for the app
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert("", "end", values=(task,))
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected_item = task_list.selection()
    if selected_item:
        task_list.delete(selected_item)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_done():
    selected_item = task_list.selection()
    if selected_item:
        task = task_list.item(selected_item, "values")[0]
        task_list.item(selected_item, values=(f"[Done] {task}"))
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task_item in task_list.get_children():
            task = task_list.item(task_item, "values")[0]
            file.write(task + "\n")
    messagebox.showinfo("Save Successful", "Tasks saved successfully.")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        task_list.delete(*task_list.get_children())
        for task in tasks:
            task_list.insert("", "end", values=(task.strip(),))
    else:
        messagebox.showwarning("Load Error", "No saved tasks found.")

# Create the main window
window = tk.Tk() 
window.title("Smart To-Do List")
window.geometry("500x500")
window.configure(bg="#f5f5f5")

# Set the icon
window.iconbitmap("sticky_note.ico")

# Title Label
title_label = tk.Label(window, text="Smart To-Do List", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Input frame
input_frame = tk.Frame(window, bg="#f5f5f5")
input_frame.pack(pady=10)

task_entry = ttk.Entry(input_frame, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=5)

add_btn = ttk.Button(input_frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=1, padx=10)

# Task List
task_frame = tk.Frame(window, bg="#f5f5f5")
task_frame.pack(pady=10)

task_list = ttk.Treeview(task_frame, columns=("Task"), show="headings", height=15)
task_list.heading("Task", text="Task")
task_list.column("Task", width=400, anchor="center")
task_list.pack()

# Button frame
btn_frame = tk.Frame(window, bg="#f5f5f5")
btn_frame.pack(pady=10)

done_btn = ttk.Button(btn_frame, text="Mark Done", command=mark_done)
done_btn.grid(row=0, column=0, padx=5)

delete_btn = ttk.Button(btn_frame, text="Delete Task", command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

save_btn = ttk.Button(btn_frame, text="Save Tasks", command=save_tasks)
save_btn.grid(row=0, column=2, padx=5)

load_btn = ttk.Button(btn_frame, text="Load Tasks", command=load_tasks)
load_btn.grid(row=0, column=3, padx=5)

# Run the app
window.mainloop()

#made with python