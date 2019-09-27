import tkinter as tk

class Entry(tk.Entry):
    def __init__(self, parent, placeholder='', variable=None):
        super().__init__(parent, width=35, textvariable=variable)

        self.placeholder = placeholder
        self.bind("<FocusIn>", self.on_focus)
        self.bind("<FocusOut>", self.on_unfocus)
        self.activate_placeholder()

    def on_focus(self, event):
        if self.empty():
            self.deactivate_placeholder()

    def on_unfocus(self, event):
        if self.empty():
            self.activate_placeholder()

    def activate_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = 'gray'

    def deactivate_placeholder(self):
        self.delete(0, tk.END)
        self['fg'] = 'black'

    def empty(self):
        return len(self.get()) == 0 or self.get() == self.placeholder
