from Image import Image
from PCAClass import PCAClass
from DatasetClass import DatasetClass
from ImageToMatrixClass import ImageToMatrixClass


class Performance(Image):
    def __init__(self, label, person_label, percentage_label):
        super().__init__()
        self.percentage_label = percentage_label
        self.label = label
        self.person_label = person_label
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
        correct = 0
        wrong = 0
        i = 0

        for img_path in self.imgs_paths_testing:
            img = self.PCAClass_obj.image_from_path(img_path)
            self.display_image(img)
            new_coords_for_img = self.PCAClass_obj.new_coord(img)

            finded_name = self.PCAClass_obj.recognize_face(new_coords_for_img)
            target_index = self.labels_imgs_testing[i]
            original_name = self.images_targets[target_index]

            if finded_name is original_name:
                correct += 1
                self.label.setText(f"Correct Result, Name: {finded_name}")

            else:
                wrong += 1
                self.label.setText(f"Wrong Result, Name: {finded_name}")
            i += 1

        self.label.setText(f"Total Correct {correct}")
        self.person_label.setText(f"Total Wrong {wrong}")
        self.percentage_label.setText(
            f"Percentage {correct / (correct + wrong) * 100}")
