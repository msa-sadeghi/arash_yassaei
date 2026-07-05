import customtkinter as ctk
import tkinter as tk


def add_item():
    listbox.insert(tk.END, text_var.get())


root = ctk.CTk()
text_var = tk.StringVar()
entry = ctk.CTkEntry(root, width=300, textvariable=text_var)
entry.pack()
my_button = ctk.CTkButton(root, text="click me", command=add_item)
my_button.pack()

listbox = tk.Listbox(
    root,
    fg="#2c3e50",
    bg="#fafafa",
    font=("Arial", 11),
    highlightbackground="#3498db",
    highlightthickness=1,
    highlightcolor="#3498db",
    width=40,
    height=10,
)
listbox.pack()
listbox.insert(tk.END, "buy paper")
listbox.insert(tk.END, "buy iphone")

root.mainloop()
