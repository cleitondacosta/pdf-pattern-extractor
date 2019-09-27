import tkinter as tk

from view.PDFArea import PDFArea
from view.SearchArea import SearchArea

from controller.MainSceneController import MainSceneController as Controller

from functools import partial

class MainScene(tk.Frame):
    def __init__(self, master=None):
        self.create_window(master)
        self.create_root_layout()
        self.create_widgets()
        self.create_controller()
        self.put_widgets_in_layout()
        self.bind_events()

    def create_window(self, master):
        super().__init__(master)
        self.master = master

    def create_root_layout(self):
        self.pack(padx=(5, 5), pady=(5, 5))

    def create_widgets(self):
        self.pdf_area = PDFArea(self)
        self.search_area = SearchArea(self)
        self.extract_button = tk.Button(self, text="Extract pages")

    def create_controller(self):
        self.controller = Controller(self.pdf_area.files)

        self.controller.configure_search(
            self.search_area.pattern,
            self.search_area.case_sensitive,
            self.search_area.pattern_as_regex
        )

    def put_widgets_in_layout(self):
        self.pdf_area.pack(fill="both", expand=True)
        self.search_area.pack(fill="both", expand=True)
        self.extract_button.pack(fill="both", expand=True)

    def bind_events(self):
        self.extract_button['command'] = partial(
            self.controller.extract_button_action,
            self
        )
