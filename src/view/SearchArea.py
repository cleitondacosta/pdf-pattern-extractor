import tkinter as tk

from view.LabelSeparator import LabelSeparator
from view.Entry import Entry

class SearchArea(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pattern = tk.StringVar()
        self.case_sensitive = tk.IntVar()
        self.pattern_as_regex = tk.IntVar()

        self.create_widgets()
        self.create_layout()
        self.put_widgets_in_layout()

    def create_widgets(self):
        self.label = LabelSeparator(self, text="Search options")
        self.entry = Entry(self, placeholder="Text to search", variable=self.pattern)
        self.regex_checkbox = tk.Checkbutton(self, text="Interpret as regex",
                                             variable=self.pattern_as_regex)
        self.sensitive_checkbox = tk.Checkbutton(self, text="Case sensitive",
                                                 variable=self.case_sensitive)

    def create_layout(self):
        self.pack()

    def put_widgets_in_layout(self):
        self.label.pack(fill="both")
        self.entry.pack(fill="both")
        self.regex_checkbox.pack(anchor='w', pady=(3, 0))
        self.sensitive_checkbox.pack(anchor='w', pady=(0, 3))

    def pattern_entry_empty(self):
        return self.entry.empty()
