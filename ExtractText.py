from PyQt5.QtWidgets import QMessageBox
from PIL import Image
import pytesseract


def extract_image_text(self):
    if self.file_path != "":
        # Creating list of allowed extension
        file_format = ['.jpg', '.jpeg', '.JPEG', '.JPG', '.png', '.PNG', '.tif', '.TIF']

        # Extracting the extension from the filepath
        pos = self.file_path.index('.')
        # Checking if the extension is valid
        if self.file_path[pos:] in file_format:

            image = Image.open(self.file_path)
            # Converting Image to String using OCR
            text = pytesseract.image_to_string(image)
            if text == "":
                self.textbox.setText("Empty Page!!")
            else:
                self.textbox.setText(text)
        else:

            QMessageBox.question(self, 'Error!', 'Invalid file format selected. (Allowed formats: JPG ,JPEG ,PNG ,TIF )'
                                 ,QMessageBox.Ok, QMessageBox.Ok)
    else:

        error_message = \
            '''
No file selected!
Please select the file first before extracting.

            '''
        QMessageBox.question(self, 'Error!', error_message, QMessageBox.Ok, QMessageBox.Ok)
