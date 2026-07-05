import customtkinter as ctk
import tkinter as tk


def add_item():
    listbox.insert(tk.END, text_var.get())

def on_select(e):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        item = listbox.get(index)
        output_var.set(item)

root = ctk.CTk()
output_var = tk.StringVar()
output = tk.Label(root, textvariable=output_var)
output.pack()
text_var = tk.StringVar()
entry = ctk.CTkEntry(root, width=300, textvariable=text_var)
entry.pack()
my_button = ctk.CTkButton(root, text="click me", command=add_item)
my_button.pack()
scrollbar = ctk.CTkScrollbar(root)
scrollbar.pack(side="right", fill="y")
listbox = tk.Listbox(
    root,
    fg="#2c3e50",
    bg="#fafafa",
    font=("Arial", 21),
    highlightbackground="#3498db",
    highlightthickness=1,
    highlightcolor="#3498db",
    yscrollcommand=scrollbar.set,
    width=40,
    height=10,
)
listbox.pack(side="left", fill="both", expand=True)
scrollbar.configure(command=listbox.yview)
for i in range(1, 21):
    listbox.insert(tk.END, f"job number {i}")


listbox.see(tk.END)
listbox.bind("<<ListboxSelect>>", on_select)
root.mainloop()
