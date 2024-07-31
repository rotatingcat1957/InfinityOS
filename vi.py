# Import the modules
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Create the main window
root = tk.Tk()
root.title("Text Editor")

# Create the text area
text = tk.Text(root)
text.pack(expand=True, fill="both")

# Create the menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# Create the file menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

# Define the file name variable
file_name = None

# Define the new file function
def new_file():
    global file_name
    file_name = None
    text.delete(1.0, "end")
    root.title("Text Editor")

# Define the open file function
def open_file():
    global file_name
    file_name = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if file_name:
        text.delete(1.0, "end")
        with open(file_name, "r") as f:
            text.insert(1.0, f.read())
        root.title(os.path.basename(file_name))

# Define the save file function
def save_file():
    global file_name
    if file_name:
        with open(file_name, "w") as f:
            f.write(text.get(1.0, "end"))
        messagebox.showinfo(title="Save File", message="File saved successfully")
    else:
        save_as_file()

# Define the save as file function
def save_as_file():
    global file_name
    file_name = filedialog.asksaveasfilename(title="Save File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if file_name:
        with open(file_name, "w") as f:
            f.write(text.get(1.0, "end"))
        root.title(os.path.basename(file_name))
        messagebox.showinfo(title="Save File", message="File saved successfully")

# Add the file menu commands
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Run the main loop
root.mainloop()
