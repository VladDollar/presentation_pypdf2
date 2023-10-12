import PyPDF2
from PIL import Image
import io
import os


class PDFImageExtractor:
    def __init__(self, pdf_file_path, output_folder):
        self._pdf_file_path = pdf_file_path
        self._output_folder = output_folder

    def extract_images(self):
        try:
            os.makedirs(self._output_folder, exist_ok=True)

            with open(self._pdf_file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)

                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)

                    if '/XObject' in page['/Resources']:
                        xObject = page['/Resources']['/XObject'].get_object()
                        for obj in xObject:
                            try:
                                if xObject[obj]['/Subtype'] == '/Image':

                                    # Получаем данные изображения
                                    data = xObject[obj].get_data()
                                    img_data = io.BytesIO(data)

                                    if '/Filter' in xObject[obj]:
                                        if xObject[obj]['/Filter'] == '/FlateDecode':
                                            # Если есть фильтр FlateDecode, извлекаем изображение и сохраняем как PNG
                                            img = Image.open(img_data)
                                            img.save(os.path.join(self._output_folder,
                                                                  f'page_{page_num + 1}_{obj[1:]}.png'))
                                        elif xObject[obj]['/Filter'] == '/DCTDecode':
                                            # Если есть фильтр DCTDecode, сохраняем как JPEG
                                            with open(os.path.join(self._output_folder,
                                                                   f'page_{page_num + 1}_{obj[1:]}.jpg'), "wb") as img:
                                                img.write(data)
                                        elif xObject[obj]['/Filter'] == '/JPXDecode':
                                            # Если есть фильтр JPXDecode, сохраняем как JP2
                                            with open(os.path.join(self._output_folder,
                                                                   f'page_{page_num + 1}_{obj[1:]}.jp2'), "wb") as img:
                                                img.write(data)
                                        elif xObject[obj]['/Filter'] == '/CCITTFaxDecode':
                                            # Если есть фильтр CCITTFaxDecode, сохраняем как TIFF
                                            with open(os.path.join(self._output_folder,
                                                                   f'page_{page_num + 1}_{obj[1:]}.tiff'), "wb") as img:
                                                img.write(data)
                                    else:
                                        # Если фильтра нет, извлекаем изображение и сохраняем как PNG
                                        img = Image.open(img_data)
                                        img.save(os.path.join(self._output_folder,
                                                              f'page_{page_num + 1}_{obj[1:]}.png'))
                            except:
                                pass
        except Exception as e:
            print(f"An error occurred: {str(e)}")
