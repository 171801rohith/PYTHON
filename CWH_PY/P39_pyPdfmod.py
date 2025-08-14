# Merging pdf files with PyPDF2 module

from PyPDF2 import PdfWriter  # type: ignore (install neccessary packages)
import os

merger = PdfWriter()
dir = "R:\\Web_Technologies_Notes\\Biology"
files = sorted(os.listdir(dir))
print(files)
for pdf in files:
    if pdf == "2.pdf" or pdf == "3.pdf":
        print(pdf)
        full_path = os.path.join(dir, pdf)
        merger.append(full_path)

merger.write("R:\\Web_Technologies_Notes\\Biology\\Module_4.pdf")
merger.close()
