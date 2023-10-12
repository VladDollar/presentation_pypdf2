import presentation_pypdf2

input_pdf = 'data/input.pdf'
output_pdf = 'data/output.pdf'
watermark_pdf = 'data/watermark.pdf'

output_folder = 'output_images'

# Вычисление хэша
computed_hash = presentation_pypdf2. \
    PDFHashCalculator(input_pdf).calculate_pdf_hash()

print(computed_hash)

# Извлечение картинок
presentation_pypdf2. \
    PDFImageExtractor(input_pdf, output_folder).extract_images()

# Добавление водяных знаков
presentation_pypdf2.PDFWatermarker(
    input_pdf, output_pdf, watermark_pdf
).add_watermark()

# извлечение метаданных
pdf_extractor = presentation_pypdf2.PDFMetadataExtractor(input_pdf)
metadata = pdf_extractor.extract_metadata()
pdf_extractor.pretty_print_metadata(metadata)

# поворот изображений
output_pdf = 'data/rotated.pdf'
presentation_pypdf2.PDFRotator(input_pdf, output_pdf).rotate_pages()

# разделение по странице
output_folder = 'output_pages'
presentation_pypdf2.PDFSplitter(input_pdf, output_folder).split_pdf_pages()
