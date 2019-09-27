import PyPDF2
import re
from controller.SearchUtils import contains_text
from controller.SearchUtils import contains_regex

class PDFPatternExtractor:
    def __init__(self, pdf_filenames=[]):
        self.pdf_filenames = pdf_filenames
        self.pattern = ''
        self.case_sensitive = False
        self.pattern_as_regex = False
        self.callback = None

    def set_pdf_filenames(self, pdf_filenames):
        self.pdf_filenames = pdf_filenames

    def set_pattern(self, pattern):
        self.pattern = pattern

    def set_pattern_as_regex(self, pattern_as_regex):
        self.pattern_as_regex = pattern_as_regex

    def set_case_sensitive(self, case_sensitive):
        self.case_sensitive = case_sensitive

    def set_callback(self, callback):
        """Set the callback function, which is called sometimes in
        extract_to_one_pdf(). This is optional.

        The callback function must receive 3 arguments:
        filename -- Stores the current filename. It can be None.
        page_num -- Stores the current page number. It can be None.
        event -- String that represents a part of the process. It's never None.

        event can be: 'pdf iterated', 'page iterated', 'writing pdf',
                      'closing files', 'pattern found', 'pattern not found',
                      'nothing found', 'done'
        """
        self.callback = callback

    def extract_to_one_pdf(self, output_filename):
        files = [open(pdf_file, 'rb') for pdf_file in self.pdf_filenames]
        pdfs = [PyPDF2.PdfFileReader(f) for f in files]
        pdf_writer = PyPDF2.PdfFileWriter()

        for filename, pdf in zip(self.pdf_filenames, pdfs):
            self.exec_callback(filename, None, 'pdf iterated')

            for page_num in range(pdf.getNumPages()):
                self.exec_callback(filename, page_num, 'page iterated')

                if self.pdf_page_contains_pattern(pdf.getPage(page_num)):
                    pdf_writer.addPage(pdf.getPage(page_num))
                    self.exec_callback(filename, page_num, 'pattern found')
                else:
                    self.exec_callback(filename, page_num, 'pattern not found')

        if pdf_writer.getNumPages() > 0:
            with open(output_filename, 'wb') as output_file:
                self.exec_callback(None, None, 'writing pdf')
                pdf_writer.write(output_file)
        else:
            self.exec_callback(filename, None, 'nothing found')

        for f in files:
            self.exec_callback(None, None, 'closing files')
            f.close()

        self.exec_callback(None, None, 'done')

    def pdf_page_contains_pattern(self, pdf_page):
        try:
            text = pdf_page.extractText()

            if self.pattern_as_regex:
                return contains_regex(text, self.pattern, self.case_sensitive)
            else:
                return contains_text(text, self.pattern, self.case_sensitive)
        except:
            return False

    def exec_callback(self, filename, page_num, event):
        if self.callback:
            self.callback(filename, page_num, event)

    def __str__(self):
        return 'class PDFPatternExtractor:\n'\
                + f'    pdf_filenames: {self.pdf_filenames}\n'\
                + f'    pattern: "{self.pattern}"\n'\
                + f'    case_sensitive: {self.case_sensitive}\n'\
                + f'    pattern_as_regex: {self.pattern_as_regex}\n'
