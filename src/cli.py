#!/usr/bin/env python3

from controller.PDFPatternExtractor import PDFPatternExtractor
import sys
from os.path import exists

def main():
    if len(sys.argv) < 4:
        print('Usage: cli.py PATTERN OUTPUT_FILENAME PDF_FILE...')
        sys.exit(1)

    pattern = sys.argv[1]
    output_filename = sys.argv[2]
    pdfs = sys.argv[3:]

    if exists(output_filename):
        print(f'Error: OUTPUT_FILENAME "{output_filename}" already exists')
        sys.exit(1)

    must_exit = False
    for pdf in pdfs:
        if not exists(pdf):
            print(f'Error: File "{pdf}" does not exists.')
            must_exit = True

    if must_exit:
        sys.exit(1)

    pdf_pattern_extractor = PDFPatternExtractor(pdfs)
    pdf_pattern_extractor.set_pattern_as_regex(True)
    pdf_pattern_extractor.set_pattern(pattern)
    pdf_pattern_extractor.set_callback(callback)

    print(pdf_pattern_extractor)

    pdf_pattern_extractor.extract_to_one_pdf(output_filename)

def callback(filename, page_num, event):
    if event == 'pdf iterated':
        print(f'\n:: {filename} ::')

    if event == 'page iterated':
        print(f'    page: {page_num}', end='\r')

    if event == 'pattern found':
        print(f'\n    pattern found in page {page_num}')

    if event == 'writing pdf':
        print('\nSaving output file ...')

    if event == 'nothing found':
        print('\nNothing found.')

    if event == 'done':
        print('Done.\n')

if __name__ == '__main__':
    main()
