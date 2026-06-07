import tkinter as tk
from tkinter import ttk

window = tk.Tk()

x = window.winfo_screenwidth() // 2 - 200
y = window.winfo_screenheight() // 2 - 150

window.geometry(f"400x300+{x}+{y}")
main_frame = ttk.Frame(window)

main_frame.pack(fill="both", expand=True)

style = ttk.Style(master=main_frame)
style.configure("TFrame", background="#f4f6f9")
style.configure(".", font=("arial", 22))
tk.mainloop()
