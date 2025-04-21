import fitz  # PyMuPDF module problem

# File_path = '/Users/jack/Downloads/Export 3.pdf'

def Extract_pdf_heading(Pdf_path, page):
    # PDF处理获取页数
    doc = fitz.open(Pdf_path)
    page_text = doc.get_page_text(page)
    txt = str(page_text)
    if txt != '':
        text = txt.splitlines()[0]
        return text
    # with open('test.txt', 'w') as file:
    #     file.write(page_text)
    # with open('test.txt', 'r') as read:
    #     line_1 = read.readline()
    #     return line_1

# Extract_pdf_heading(File_path, 0)






