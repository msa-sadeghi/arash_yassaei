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
        self._build_input()
        self._build_list()
        # self._build_actions()
        # self._build_footer()

    def _build_header(self):
        hdr = tk.Frame(self.root, bg=COLORS["bg_header"], height=70)
        hdr.pack(fill="x")
        tk.Label(hdr, text="TODO LIST", bg=COLORS["bg_header"], fg=COLORS["white"], font=("Tahoma", 18, "bold")).place(
            relx=0.5, rely=0.5, anchor="center"
        )

    def _build_search(self):
        search_bar = tk.Frame(self.root, bg=COLORS["bg_search"], pady=8, padx=12)
        search_bar.pack(fill="x")
        tk.Label(search_bar, text="search", bg=COLORS["bg_search"], fg=COLORS["white"]).pack(side="left")
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(search_bar, textvariable=self.search_var)
        self.search_entry.pack(side="left", fill="x", expand=True, ipady=4, padx=6)

    def _build_input(self):
        inp = tk.Frame(self.root, bg=COLORS["bg_root"], pady=8, padx=12)
        inp.pack(fill="x")
        self.task_entry = tk.Entry(inp)
        self.task_entry.pack(side="left", fill="x", expand=True, ipady=4, padx=6)

        self.priority_var = tk.StringVar(value="معمولی")
        priority_frame = tk.Frame(inp, bg=COLORS["bg_root"])
        priority_frame.pack(side="left")

        self.priority_menu = tk.OptionMenu(priority_frame, self.priority_var, *PRIORITY)
        self.priority_menu.pack()

        self.add_btn = tk.Button(inp, text="+", bg=COLORS["accent_lt"], fg=COLORS["white"], command=self.cmd_add)
        self.add_btn.pack(side="left")

    def _build_list(self):
        list_outer = tk.Frame(self.root, bg=COLORS["bg_root"], padx=12)
        list_outer.pack(fill="both", expand=True)
        inner = tk.Frame(list_outer, bg=COLORS["bg_list"], highlightthickness=1, highlightbackground="red")
        inner.pack(fill="both", expand=True)

        sb = tk.Scrollbar(inner)
        sb.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            inner,
            font=("Tahoma", 12),
            bg=COLORS["bg_list"],
            fg=COLORS["text_main"],
            yscrollcommand=sb.set,
            cursor="hand2",
        )
        self.listbox.pack(side="left", fill="both", expand=True, padx=4, pady=4)
        sb.config(command=self.listbox.yview)

    def cmd_add(self):
        pass
