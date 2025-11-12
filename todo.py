import tkinter as tk
import customtkinter as ctk
#importing both because of problems down the line
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue") 

tasks = []
#redid the code but with tkinter 
def view_tasks():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        listbox.insert(tk.END, f"{i}. {task}")

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        entry.delete(0, tk.END)
        view_tasks()

def remove_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        view_tasks()

#custom GUI for the app itself
app = ctk.CTk()
app.title("Modern To-Do List")

frame = ctk.CTkFrame(app)
frame.pack(padx=10, pady=10)

entry = ctk.CTkEntry(frame, width=250, placeholder_text="Enter a task...")
entry.pack(side="left", padx=5)

add_btn = ctk.CTkButton(frame, text="Add", command=add_task)
add_btn.pack(side="left", padx=5)

remove_btn = ctk.CTkButton(frame, text="Remove", command=remove_task)
remove_btn.pack(side="left", padx=5)

#used normal listbox as custom tkinter doesnt have its own
listbox = tk.Listbox(app, width=40, height=10)
listbox.pack(padx=10, pady=10)
