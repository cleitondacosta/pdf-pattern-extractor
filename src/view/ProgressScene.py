import tkinter as tk

from view.ProgressLabel import ProgressLabel
from controller.ProgressSceneController import ProgressSceneController

class ProgressScene(tk.Frame):
    def __init__(self, parent, output_filename, pdf_extractor):
        self.parent = parent
        super().__init__(self.parent)

        self.create_widgets()
        self.create_controller(pdf_extractor)
        self.create_layout()
        self.put_widgets_in_layout()
        self.bind_events()

        self.controller.start_pdf_extraction(output_filename)

    def create_widgets(self):
        self.progress_label = ProgressLabel(self)
        self.button = tk.Button(self, text='Ok', state='disabled')

    def create_controller(self, pdf_extractor):
        self.controller = ProgressSceneController(self.parent,
                                                  pdf_extractor,
                                                  self.progress_label,
                                                  self.button)

    def create_layout(self):
        self.pack(padx=(10, 10), pady=(10, 10), fill='both', expand=True)
        self.pack_propagate(0)

    def put_widgets_in_layout(self):
        self.progress_label.pack(padx=(30, 30), pady=(30, 30))
        self.button.pack(fill='both')

    def bind_events(self):
        self.button['command'] = self.controller.button_action
