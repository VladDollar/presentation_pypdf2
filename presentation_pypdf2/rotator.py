import PyPDF2


class PDFRotator:
    def __init__(self, input_file, output_file):
        self._input_file = input_file
        self._output_file = output_file

    def rotate_pages(self):
        try:
            pdf_reader = PyPDF2.PdfFileReader(open(self._input_file, 'rb'))
            pdf_writer = PyPDF2.PdfFileWriter()

            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                page.rotateClockwise(90)
                pdf_writer.addPage(page)

            with open(self._output_file, 'wb') as rotated_pdf:
                pdf_writer.write(rotated_pdf)
        except:
            pass

        print('Поворот завершен.')
