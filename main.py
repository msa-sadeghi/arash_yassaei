# import tkinter as tk
# from tkinter import ttk

# window = tk.Tk()
# def change_text():
#     # my_label.config(text="سلام چطوری")
#     my_label["text"] = name_value.get()

# def disable_button():
#     btn.config(state="disabled")

# my_label = tk.Label(window,
#     text="sample text",
#     font=("tahoma", 16),
#     fg="white",
#     bg="darkblue",
#     width=20,
#     height=2,
#     padx=10,
#     pady=5)
# my_label.pack()

# name_value = tk.StringVar()

# name_entry = tk.Entry(window, textvariable=name_value, width=30)
# name_entry.pack()
# tk.Button(window, text="change name", command=change_text).pack()
# btn = tk.Button(window, text="my button", command=disable_button)
# btn.pack()
# tk.mainloop()


# import tkinter as tk
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *

# window = ttk.Window(themename="cosmo")
# window.geometry("300x180")
# first_frame = ttk.Frame(window)
# username_label = ttk.Label(first_frame, text="username")
# username_label.pack(side="left")
# username_entry = ttk.Entry(first_frame)
# username_entry.pack(side="left")
# first_frame.pack(pady=10)

# second_frame = ttk.Frame(window)
# password_label = ttk.Label(second_frame, text="password")
# password_label.pack(side="left")
# password_entry = ttk.Entry(second_frame)
# password_entry.pack(side="left")
# second_frame.pack(pady=10)

# third_frame = ttk.Frame(window)
# login_btn = ttk.Button(third_frame, text="login")
# login_btn.pack(side="left", padx=5)
# exit_btn = ttk.Button(third_frame, text="exit", command=window.destroy)
# exit_btn.pack(side="left", padx=5)
# third_frame.pack(pady=10)


# window.mainloop()

# تمرین پایانی جلسه ۱
# برای جمع‌بندی، این برنامه را خودت بنویس (سعی کن بدون نگاه کردن به کدهای بالا):
# پنجره‌ای بساز با این مشخصات:

# عنوان پنجره: "تمرین جلسه اول"
# اندازه: 350x250
# یک Frame بالایی با یک Label که عنوان "فرم ثبت نام" را نشان دهد
# یک Frame پایینی شامل:

# یک Entry برای دریافت نام
# یک Button با متن "ثبت" که با کلیک، متن داخل Entry را در ترمینال چاپ کند و سپس Entry را خالی کند


# import tkinter as tk

# root = tk.Tk()
# root.title("sample")

# root.geometry("300x250")

# tk.Label(root, text="row 1", bg="lightblue").pack(fill="both", expand=True, side="left")
# tk.Label(root, text="row 2", bg="lightgreen").pack(fill="both", side="left")
# tk.Label(root, text="row 3", bg="lightyellow").pack(fill="both", side="left")


# root.mainloop()


# import tkinter as tk
# from ttkbootstrap.constants import *
# import ttkbootstrap as ttk

# root = ttk.Window(themename="cosmo")
# root.geometry("300x150")
# tk.Label(root, text="name").grid(row=0, column=0, padx=10, pady=10)
# tk.Entry(root).grid(row=0, column=1, padx=10, pady=10)

# tk.Label(root, text="family").grid(row=1, column=0, padx=10, pady=10)
# tk.Entry(root).grid(row=1, column=1, padx=10, pady=10)

# tk.Button(root, text="register").grid(row=2, column=0, columnspan=2, ipadx=40, sticky="nswe")

# root.mainloop()


import tkinter as tk

root = tk.Tk()
root.geometry("300x150")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
# بدون sticky - وسط سلول قرار می‌گیرد
tk.Label(root, text="بدون sticky", bg="lightcoral").grid(row=0, column=0, padx=5, pady=5)

# sticky="w" - به سمت چپ سلول می‌چسبد
tk.Label(root, text="sticky=w", bg="lightblue").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Label(root, text="sticky=e", bg="lightblue").grid(row=1, column=0, padx=5, pady=5, sticky="e")

# sticky="ew" - عرض کامل سلول را پر می‌کند
tk.Label(root, text="sticky=ew", bg="lightgreen").grid(row=2, column=0, padx=5, pady=5, sticky="ewns")

root.mainloop()
