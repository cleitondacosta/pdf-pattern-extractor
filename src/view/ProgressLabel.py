import tkinter as tk

class ProgressLabel(tk.Label):
    def __init__(self, parent):
        self.text_var = tk.StringVar()
        super().__init__(parent, textvariable=self.text_var)
        self['wraplength'] = 350
        self.pack()

    def change_text(self, text):
        self.text_var.set(text)
