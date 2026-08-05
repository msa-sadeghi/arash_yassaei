from constants import *
import tkinter as tk


class TodoApp:
    def __init__(self, root, manager):
        self.root = root
        self.manager = manager
        self._setup_window()
        self._build_ui()

    def _setup_window(self):
        self.root.title("Todo List")
        self.root.geometry("500x620")
        self.root.minsize(400, 450)
        self.root.configure(bg=COLORS["bg_root"])
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.root.geometry(f"+{x}+{y}")

    def _build_ui(self):
        self._build_header()
        self._build_search()
        # self._build_input()
        # self._build_list()
        # self._build_actions()
        # self._build_footer()

    def _build_header(self):
        hdr = tk.Frame(self.root, bg=COLORS["bg_header"], height=70)
        hdr.pack(fill="x")
        tk.Label(hdr, text="TODO LIST", bg=COLORS["bg_header"], fg=COLORS["white"], font=("Tahoma", 18, "bold")).place(
            relx=0.5, rely=0.5, anchor="center"
        )
