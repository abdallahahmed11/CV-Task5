import cv2
from Image import Image
from PCAClass import PCAClass
from DatasetClass import DatasetClass
from imageToMatrixClass import ImageToMatrixClass


class Predictor(Image):
    def __init__(self):
        super().__init__()
        self.img_width, self.img_height = 50, 50
        self.num_of_imgs_for_person = 8
        self.dataset_obj = DatasetClass(self.num_of_imgs_for_person)

        self.imgs_paths_training = self.dataset_obj.images_path_training
        self.labels_imgs_training = self.dataset_obj.labels_for_training
        self.num_of_elements_training = self.dataset_obj.num_of_images_training

        self.imgs_paths_testing = self.dataset_obj.images_path_testing
        self.labels_imgs_testing = self.dataset_obj.labels_for_testing
        self.num_of_elements_testing = self.dataset_obj.num_of_images_testing

        self.images_targets = self.dataset_obj.images_target

        self.ImageToMatrixClass_obj = ImageToMatrixClass(
            self.imgs_paths_training, self.img_height, self.img_width)

        self.img_matrix = self.ImageToMatrixClass_obj.get_matrix()
        self.PCAClass_obj = PCAClass(self.img_matrix, self.labels_imgs_training, self.images_targets,
                                     self.img_height, self.img_width, self.num_of_elements_training, quality_percent=90)

        self.new_coord = self.PCAClass_obj.reduce_dim()

    def predict(self, img_path):
        face_cascade = cv2.CascadeClassifier(
            "cascaded\data\haarcascade_frontalface_alt2.xml")

        frame = cv2.imread(img_path)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.5, minNeighbors=3)

        i = 0

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            scaled = cv2.resize(roi_gray, (self.img_height, self.img_width))
            rec_color = (0, 255, 0)
            rec_stroke = 2
            cv2.rectangle(frame, (x, y), (x+w, y+h), rec_color, rec_stroke)

            new_cord = self.PCAClass_obj.new_coord(scaled)
            name = self.PCAClass_obj.recognize_face(new_cord)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_color = (255, 0, 0)
            font_stroke = 2
            cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        font_color, font_stroke)
            print(name)
            i += 1

        # frame = cv2.resize(frame, (1080, 568))
        frame = cv2.cvtColor(
            frame, cv2.COLOR_BGR2RGB)
        return frame
