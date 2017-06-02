import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox, QLabel, QCheckBox , QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
from MenuBar import menu_bar


class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.title = 'Image Text Extractor'
        self.left = 500
        self.top = 200
        self.width = 550
        self.height = 230
        self.label = ""
        self.file_location = ""
        self.textbox = ""
        self.file_path = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        menu_bar(self)

        # Setting up info text
        self.label = QLabel("Text", self)
        self.label.setText("Please select the image you want to extract text..")
        self.label.move(45,50)
        font = QtGui.QFont("Times", 11, QFont.Bold)
        self.label.setFont(font)
        self.label.adjustSize()

        # Creating Label for selected file location
        self.file_location = QLabel("File Location", self)
        self.file_location.move(45,70)
        self.file_location.setFixedWidth(1000)
        self.file_location.adjustSize()

        # Creating Choose Image Button
        button = QPushButton('Choose Image', self)  # Create a button with label
        button.setToolTip('Click here to choose file') # The button tooltip
        button.move(420,45)
        button.clicked.connect(self.file_selection) # connects to the function that will be executed on click

        # Creating Extract button
        button_extract = QPushButton('Extract', self)  # Create a button with label
        button_extract.setToolTip('Click here to extract text from file') # The button tooltip
        button_extract.move(420,85)
        button_extract.clicked.connect(self.extratct_text) # connects to the function that will be executed on click

        ''' Commenting for this version
        self.checkbox = QCheckBox('Do you want to create the text file', self)
        self.checkbox.move(48, 90)
        self.checkbox.adjustSize()

        #self.checkbox.stateChanged.connect(self.text_file)
        '''
        # Creating Text Box field
        self.textbox = QTextEdit(self)
        self.textbox.move(20, 125)
        self.textbox.resize(500,80)

        # Displaying the the UI
        self.show()

    @pyqtSlot()
    def help_tips(self):
        help_msg = '''
        This tool will help you to extract the entire text from the selected image.
        1. Select the file whose text you want to extract.
        2. Click on Extract text button
        3. The Extracted text will be displayed in the application textbox
        '''
        QMessageBox.question(self, 'Help - Image Text Extractor', help_msg, QMessageBox.Ok, QMessageBox.Ok)

    # Selection of file on click on Choose Image Button
    @pyqtSlot()
    def file_selection(self):
        from ChooseFile import choose_image
        choose_image(self)

    # Extraction of text from Image on click of Extract button
    @pyqtSlot()
    def extratct_text(self):
        from ExtractText import extract_image_text
        extract_image_text(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())