from ui_layer import TodoApp
import tkinter as tk
from logic_layer import TaskManager
from data_layer import TaskStorage
from constants import *
storage = TaskStorage(SAVE_FILE)
manager = TaskManager(storage)
root = tk.Tk()
app = TodoApp(root,manager)


root.mainloop()
