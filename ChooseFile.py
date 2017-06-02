from PyQt5.QtWidgets import QFileDialog


def choose_image(self):

    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self,"Choose FIle", "","All Files (*);;JPEG Files (*.jpg);;PNG Files(*.png)", options=options)
    if fileName:
        self.file_path = fileName
        self.file_location.setText(self.file_path)