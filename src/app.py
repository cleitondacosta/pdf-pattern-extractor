#!/usr/bin/env python3

import tkinter as tk

from view.MainScene import MainScene

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("pdf extractor")
        self.resizable(0, 0)
        self.mainscene = MainScene(self)

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()
