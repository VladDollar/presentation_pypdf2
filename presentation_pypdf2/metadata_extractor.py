import PyPDF2
from prettytable import PrettyTable


class PDFMetadataExtractor:
    # Колонки вывода
    _table_fields = ["Параметр", "Значение"]

    def __init__(self, pdf_file_path):
        self._pdf_file_path = pdf_file_path

    def extract_metadata(self):
        try:
            with open(self._pdf_file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)  # объект ридера
                metadata = pdf_reader.getDocumentInfo()  # извлеченная информация

                return [
                    (key, value) for key, value in metadata.items()
                ]

        except FileNotFoundError:
            return None

    @classmethod
    def pretty_print_metadata(cls, metadata_list):
        if not metadata_list:
            print("Нет метаданных.")
            return

        # просто красивый вывод
        table = PrettyTable()
        table.field_names = cls._table_fields

        # настройка отображения вывода
        for field in cls._table_fields:
            table.align[field] = "l"  # Выравнивание по левому краю
            table.max_width[field] = 50  # Максимальная ширина

        table.padding_width = 1

        for key, value in metadata_list:
            table.add_row([key, value])

        print(table)
