import cv2
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Image(FigureCanvas):
    def __init__(self):
        self.img_copy = None
        self.img_original = None
        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        super().__init__(self.figure)
        self.ax.axis('off')

    def read_image(self):
        self.file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Image Files (*.png *.jpg *.bmp);;All Files (*)",
        )
        if self.file_path:
            self.img_original = cv2.imread(self.file_path)
            self.img_original = cv2.cvtColor(
                self.img_original, cv2.COLOR_BGR2RGB)
            self.img_copy = self.img_original.copy()
            self.convert_to_grey_scale()
            self.display_image(self.img_original)

    def display_image(self, img):
        self.ax.clear()
        self.figure.subplots_adjust(left=0, right=1, bottom=0, top=1)
        self.ax.imshow(img)
        self.ax.axis('off')
        self.draw_idle()

    def convert_to_grey_scale(self):
        self.img_copy = cv2.cvtColor(self.img_copy, cv2.COLOR_RGB2GRAY)

    def reset_changes(self):
        self.img_copy = self.img_original
        self.convert_to_grey_scale()
        self.display_image(self.img_copy)
