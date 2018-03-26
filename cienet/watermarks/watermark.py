#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

orig_pdf = sys.argv[1]
watermark_pdf = sys.argv[2]

output_pdf = PdfFileWriter()
output_pdf_name = orig_pdf.replace('.pdf', '.wm.pdf')

input_pdf = PdfFileReader(open(orig_pdf, "rb"))
watermark = PdfFileReader(open(watermark_pdf, "rb"))

page_count = input_pdf.getNumPages()

for index in range(0, page_count):
    input_page = input_pdf.getPage(index)
    input_page.mergePage(watermark.getPage(0))
    output_pdf.addPage(input_page)

outputStream = open(output_pdf_name, "wb")
output_pdf.write(outputStream)
outputStream.close()
