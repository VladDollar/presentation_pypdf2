import PyPDF2


class PDFWatermarker:
    def __init__(self, input_pdf, output_pdf, watermark_pdf):
        self._input_pdf = input_pdf
        self._output_pdf = output_pdf
        self._watermark_pdf = watermark_pdf

    def add_watermark(self):
        try:
            pdf_reader = PyPDF2.PdfFileReader(open(self._input_pdf, 'rb'))
            pdf_writer = PyPDF2.PdfFileWriter()
            watermark = PyPDF2.PdfFileReader(open(self._watermark_pdf, 'rb'))
            watermark_page = watermark.getPage(0)

            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                page.merge_page(watermark_page)
                pdf_writer.addPage(page)

            with open(self._output_pdf, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
        except:
            pass
