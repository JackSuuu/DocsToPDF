from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, \
    QFileDialog, QMessageBox, QMainWindow, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
import sys
from pdf_to_doc import pdf_to_doc
from Get_PDF_text import Extract_pdf_heading


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting the Vbox layout
        layout = QVBoxLayout()

        self.setWindowTitle("PDF_word Converter")
        self.setFixedWidth(600)
        self.setFixedHeight(400)
        self.setStyleSheet("background: #111111;")

        # display logo
        image = QPixmap("./PDF-WORD CONVERTER.png")
        logo = QLabel(self)
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        logo.setStyleSheet("margin-top: -150px;")
        logo.resize(300, 300)

        # Create a BUTTON WIDGET for upload image
        # 如果由多个object在图像中，需要谨慎加padding， margin。
        button = QPushButton("GENERATE")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(
            "*{border: 6px solid '#E33046';" +
            "border-radius: 35px;" +
            "font-size: 30px;" +
            "color: 'white';" +
            "padding: 15px 0;" +
            "margin: 0px 60px 35px}" +
            "*:hover{background: '#E33046';}"
        )
        button.clicked.connect(self.upload_button)
        # 直接等于函数名字，即可应用函数，不需要加括号

        # add the widget into layout
        layout.addWidget(logo)
        layout.addWidget(button)

        main_frame = QWidget()
        self.setCentralWidget(main_frame)
        main_frame.setLayout(layout)

    def upload_button(self):
        tup_pdf_file = QFileDialog.getOpenFileNames(
            self, 'open file', '/Users/jack', 'Pdf files (*.pdf)')
        print(tup_pdf_file)
        pdf_file_list = tup_pdf_file[0]
        for pdf_file in pdf_file_list:
            print(pdf_file)
            if pdf_file != '':
                Heading = Extract_pdf_heading(pdf_file, 0)
                print(Heading)
                if Heading != '':
                    output_file = '/Users/jack/Downloads/{0}.docx'.format(
                        Heading)
                    pdf_to_doc(pdf_file, output_file)
                else:
                    output_file = '/Users/jack/Downloads/output.docx'
                    pdf_to_doc(pdf_file, output_file)
            else:
                self.msg_box = QMessageBox(
                    QMessageBox.Warning, 'ERROR', 'Please choose a pdf_file first')
                self.msg_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
