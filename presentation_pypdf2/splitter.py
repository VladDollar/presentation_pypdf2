import PyPDF2
import os


class PDFSplitter:
    def __init__(self, input_pdf_path, output_directory):
        self._input_pdf_path = input_pdf_path
        self._output_directory = output_directory

    def split_pdf_pages(self):
        if not os.path.exists(self._output_directory):
            os.makedirs(self._output_directory)
        try:
            with open(self._input_pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)

                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    pdf_writer = PyPDF2.PdfFileWriter()
                    pdf_writer.addPage(page)

                    output_file_path = os.path.join(
                        self._output_directory, f'page_{page_num + 1}.pdf')

                    with open(output_file_path, 'wb') as output_file:
                        pdf_writer.write(output_file)
        except:
            pass

        print('Разделение PDF завершено.')
