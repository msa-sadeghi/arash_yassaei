import tkinter as tk

window = tk.Tk()
window.iconbitmap("icon.ico")
window.title("Task Manager")
window.resizable(False, False)
window.config(bg="#1e1e1e")
x = window.winfo_screenwidth() // 2 - 400
y = window.winfo_screenheight() // 2 - 250

window.geometry(f"800x500+{x}+{y}")


label = tk.Label(window, text="hello", font=("Arial", 24, "bold"), fg="red", bg="white")
label.pack(pady=10, ipadx=10, ipady=10)
label = tk.Label(window, text="hello", font=("Arial", 24, "bold"), fg="red", bg="#b44242")
label.pack(pady=30)

username = tk.Entry(window, font=("Arial", 24, "bold"), 
                    width=30, bg="#2b2b2b", fg="white", bd=0,
                    insertbackground="white"
                    )
username.pack()

tk.mainloop()
