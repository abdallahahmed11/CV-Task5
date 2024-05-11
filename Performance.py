from Image import Image
from PCAClass import PCAClass
from DatasetClass import DatasetClass
from ImageToMatrixClass import ImageToMatrixClass


class Performance(Image):
    def __init__(self, label, person_label, percentage_label, action_button):
        super().__init__()
        self.percentage_label = percentage_label
        self.label = label
        self.person_label = person_label
        self.action_button = action_button
        self.no_button_clicks = 0
        self.correct = 0
        self.wrong = 0
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

    def show_performace(self):
        original_names = []
        finded_names = []
        if self.no_button_clicks == 0:
            self.action_button.setText('Next')

        if (self.no_button_clicks == len(self.imgs_paths_testing)-1):
            self.action_button.hide()
            self.label.setText(f"Total correct {self.correct}")
            self.person_label.setText(f"Total wrong {self.wrong}")
            self.percentage_label.setText(
                f"Percentage {round(self.correct / (self.correct + self.wrong) * 100,2)} %")
        else:
            img = self.PCAClass_obj.image_from_path(
                self.imgs_paths_testing[self.no_button_clicks])
            self.display_image(img)
            new_coords_for_img = self.PCAClass_obj.new_coord(img)

            finded_name = self.PCAClass_obj.recognize_face(new_coords_for_img)
            finded_names.append(finded_name)
            target_index = self.labels_imgs_testing[self.no_button_clicks]
            original_name = self.images_targets[target_index]
            original_names.append(original_name)

            if finded_name is original_name:
                self.correct += 1
                self.label.setText(f"correct Result, Name: {finded_name}")

            else:
                self.wrong += 1
                self.label.setText(f"wrong Result, Name: {finded_name}")

        self.no_button_clicks += 1
