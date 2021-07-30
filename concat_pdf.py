#!/usr/bin/python3
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def concat_pdf(file1, file2, outfile):
    # Concatenate files
    pdf_writer = PdfFileWriter()
    pdf_reader_1 = PdfFileReader(file1)
    pdf_reader_2 = PdfFileReader(file2)

    for i in range(0, pdf_reader_1.numPages):
        pdf_writer.addPage(pdf_reader_1.getPage(i))
        
    for i in range(0, pdf_reader_2.numPages):
        pdf_writer.addPage(pdf_reader_2.getPage(i))

    with open(outfile, 'wb') as f:
        pdf_writer.write(f)


if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    outfile = sys.argv[3]
    concat_pdf(file1, file2, outfile)
