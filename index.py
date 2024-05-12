from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from os import path
import sys
from Init_UI import *
import cv2

FORM_CLASS, _ = loadUiType(
    path.join(path.dirname(__file__), "Face Detection.ui"
              ))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("Face recognation")
        self.setupUi(self)
        init_ui(self)

    def mouseDoubleClickEvent(self, event, img):
        if event.button() == Qt.LeftButton:
            img.read_image()

    def upload_image(self, img):
        img.read_image()

    def add_image_viewers(self, h_layout, images, images_labels):
        for i in range(len(images)):
            group_box = QGroupBox(images_labels[i])
            group_box_layout = QVBoxLayout(group_box)
            group_box_layout.addWidget(images[i])
            h_layout.addWidget(group_box)

    def Predict_button_pressed(self):
        frame = self.predictor_img_input.predict(
            self.predictor_img_input.file_path)

        self.predictor_img_input.display_image(frame)

    def performance_button_pressed(self):
        self.performance_img_input.show_performace()
    
    

    def exit_program(self):
        sys.exit()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
