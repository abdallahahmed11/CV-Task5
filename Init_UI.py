from Predictor import Predictor


def init_ui(self):
    predictor_tab(self)


def predictor_tab(self):
    self.predictor_img_input = Predictor()
    Predictor_images = [self.predictor_img_input]
    Predictor_labels = ["Image"]
    self.add_image_viewers(self.predictor_layout,
                           Predictor_images, Predictor_labels)
    # self.actionOpen.triggered.connect(lambda: self.upload_image(self.region_growing_img_input))
    self.predictor_img_input.mouseDoubleClickEvent = lambda event: self.mouseDoubleClickEvent(
        event, self.predictor_img_input)
    self.predict_button.clicked.connect(self.Predict_button_pressed)
