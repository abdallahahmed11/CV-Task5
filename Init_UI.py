from Predictor import Predictor
from Performance import Performance
from Image import Image

def init_ui(self):
    predictor_tab(self)
    performance_tab(self)


def predictor_tab(self):
    self.predictor_img_input = Predictor()
    Predictor_images = [self.predictor_img_input]
    Predictor_labels = ["Image"]
    self.add_image_viewers(self.predictor_layout,
                           Predictor_images, Predictor_labels)
    self.predictor_img_input.mouseDoubleClickEvent = lambda event: self.mouseDoubleClickEvent(
        event, self.predictor_img_input)
    self.predict_button.clicked.connect(self.Predict_button_pressed)


def performance_tab(self):
    self.performance_img_input = Performance(
        self.label, self.person_label, self.percentage_label, self.generate_button)
    # self.ROC_img = Image()
    performance_images = [self.performance_img_input]
    performance_labels = ["Image" ]
    self.add_image_viewers(self.performance_layout,
                           performance_images, performance_labels)
    self.performance_img_input.mouseDoubleClickEvent = lambda event: self.mouseDoubleClickEvent(
        event, self.performance_img_input)
    self.generate_button.clicked.connect(self.performance_button_pressed)
