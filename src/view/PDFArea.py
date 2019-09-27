import tkinter as tk
from pathlib import Path
from tkinter.filedialog import askopenfilenames

class PDFArea(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.create_layout()
        self.put_widgets_in_layout()
        self.bind_events()
        self.files = []

    def create_widgets(self):
        self.pdflistbox = tk.Listbox(self, selectmode='multiple')
        self.addbutton = tk.Button(self, text='Add file')
        self.remove_selected_button = tk.Button(self, text='Remove selected')

    def create_layout(self):
        self.pack()

    def put_widgets_in_layout(self):
        self.pdflistbox.pack(fill='both', pady=(0, 3))
        self.addbutton.pack(fill='both')
        self.remove_selected_button.pack(fill='both')

    def bind_events(self):
        self.addbutton['command'] = self.onclick_addbutton
        self.remove_selected_button['command'] = self.remove_selected_items

    def onclick_addbutton(self):
        selected_files = self.ask_user_to_select_files()
        self.add_selected_files_to_listbox(selected_files)

    def ask_user_to_select_files(self):
        home_dir = str(Path.home())
        file_types=[('pdf files', '*.pdf')]
        return askopenfilenames(initialdir=home_dir, filetypes=file_types)

    def add_selected_files_to_listbox(self, selected_files):
        for filename in selected_files:
            self.pdflistbox.insert(tk.END, Path(filename).name)
            self.files.append(filename)

    def remove_selected_items(self):
        for counter, item_index in enumerate(self.pdflistbox.curselection()):
            self.pdflistbox.delete(item_index - counter)
            self.files.pop(item_index - counter)
