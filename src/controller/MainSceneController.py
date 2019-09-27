import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename

from view.ProgressScene import ProgressScene

from controller.PDFPatternExtractor import PDFPatternExtractor

from pathlib import Path

class MainSceneController:
    def __init__(self, pdf_files):
        self.pdf_files = pdf_files
        self.pdf_extractor = PDFPatternExtractor()

    def configure_search(self, pattern, case_sensitive, pattern_as_regex):
        self.pattern = pattern
        self.case_sensitive = case_sensitive
        self.pattern_as_regex = pattern_as_regex

    def configure_pdf_extractor(self):
        self.pdf_extractor.set_pdf_filenames(self.pdf_files)
        self.pdf_extractor.set_pattern(self.pattern.get())
        self.pdf_extractor.set_case_sensitive(self.case_sensitive.get())
        self.pdf_extractor.set_pattern_as_regex(self.pattern_as_regex.get())

    def extract_button_action(self, main_scene_parent):
        if len(self.pdf_files) == 0:
            messagebox.showerror('Error', 'No pdf file selected')
            return

        if not self.pattern.get():
            messagebox.showerror('Error', 'No pattern provided')
            return

        output_filename = self.ask_user_to_select_save_file()

        if not output_filename:
            return

        self.spawn_progress_window(main_scene_parent, output_filename)

    def ask_user_to_select_save_file(self):
        filename = asksaveasfilename(
            filetypes=[("pdf file", "*.pdf")],
            defaultextension=".pdf",
            initialdir=Path.home()
        )

        if not filename:
            return ''
        else:
            return filename

    def spawn_progress_window(self, main_scene_parent, output_filename):
        def disable_close():
            pass

        progress_window = tk.Toplevel(main_scene_parent)
        progress_window.protocol('WM_DELETE_WINDOW', disable_close)
        progress_window.geometry('400x150')
        progress_window.resizable(0, 0)

        self.configure_pdf_extractor()

        progress_scene = ProgressScene(progress_window, output_filename,
                                       self.pdf_extractor)

        progress_window.grab_set()
