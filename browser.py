import tkinter as tk
from tkinterweb import *

root = tk.Tk()
root.title("Infinity Browser")
root.geometry("1280x720")
entry = tk.Entry(root)
frame = HtmlFrame(root)
frame.enable_images(True)
frame.enable_stylesheets(True)
frame.pack(fill="both", expand=True)
def load_site():
	text = entry.get()
	frame.load_website(text, force=True)
def refresh():
	root.update()
	root.update_idletasks()
entry.bind("Return", load_site)
loadbutton = tk.Button(root, text="Load page", command=load_site)
refreshbutton = tk.Button(root, text="Refresh", command=refresh)
refreshbutton.pack(side="top", anchor="nw")
loadbutton.pack(side="top", anchor="nw")
entry.pack(side="top", anchor="n")
root.mainloop()