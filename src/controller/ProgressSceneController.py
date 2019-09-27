import tkinter as tk
import threading

import os

from pathlib import Path

class PDFExtractionThread(threading.Thread):
    def __init__(self, pdf_extractor, output_filename):
        super().__init__()
        self.setDaemon(True)
        self.pdf_extractor = pdf_extractor
        self.output_filename = output_filename

    def run(self):
        self.pdf_extractor.extract_to_one_pdf(self.output_filename)


class ProgressSceneController:
    def __init__(self, parent, pdf_extractor, progress_label, button):
        self.parent = parent
        self.pdf_extractor = pdf_extractor
        self.progress_label = progress_label
        self.button = button

        self.pdf_extractor.set_callback(self.pdf_extractor_callback)
        self.number_of_patterns_found = 0

    def pdf_extractor_callback(self, filename, page_num, event):
        if event == 'page iterated':
            filename = Path(filename).name
            self.progress_label.change_text(
                f'Analyzing pages of {filename}:\n{page_num}'
            )

        if event == 'writing pdf' or event == 'closing files':
            self.progress_label.change_text('Saving ...')

        if event == 'pattern found':
            self.number_of_patterns_found += 1

        if event == 'done':
            occurrences = self.number_of_patterns_found
            self.progress_label.change_text(
                'Done. '
                + f'{occurrences} Occurrences of '
                + f'"{self.pdf_extractor.pattern}".'
            )
            self.button['state'] = 'normal'

    def start_pdf_extraction(self, output_filename):
        self.extraction_thread = PDFExtractionThread(self.pdf_extractor,
                                                output_filename)
        self.extraction_thread.start()

    def button_action(self):
        self.parent.destroy()
