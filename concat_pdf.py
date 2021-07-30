#!/usr/bin/python3
import sys
from PyPDF2 import PdfFileMerger, PdfFileWriter

def concat_pdf(file1, file2, outfile):
    # Concatenate files
    pdf_merger = PdfFileMerger()

    pdf_merger.append(file1)
    pdf_merger.append(file2)

    with open(outfile, 'wb') as f:
        pdf_merger.write(f)


if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    outfile = sys.argv[3]
    concat_pdf(file1, file2, outfile)
