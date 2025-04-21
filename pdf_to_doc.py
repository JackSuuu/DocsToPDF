from pdf2docx import Converter

# pdf_file = '/Users/jack/Downloads/早起是创作者们成功的秘诀吗？.pdf'
# docx_file = '/Users/jack/Downloads/demo.docx'


def pdf_to_doc(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()



