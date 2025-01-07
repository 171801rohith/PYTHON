# Merging pdf files with PyPDF2 module

from PyPDF2 import PdfWriter # type: ignore (install neccessary packages)
import os

merger = PdfWriter()
dir = "C:\\Users\\rohit\\Desktop\\PYTHON\\OS Example\\Tutorial2"
files = os.listdir(dir)

for pdf in files:
    if pdf.endswith(".pdf"):
        merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

