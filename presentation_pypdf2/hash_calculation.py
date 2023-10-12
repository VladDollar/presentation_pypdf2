import hashlib


class PDFHashCalculator:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def calculate_pdf_hash(self) -> str | None:
        sha256 = hashlib.sha256()

        try:
            with open(self._file_path, 'rb') as file:
                while True:
                    data = file.read(2 ** 16)  # 64 KB за итерацию
                    if not data:
                        break
                    sha256.update(data)
        except FileNotFoundError:
            return None

        return sha256.hexdigest()
