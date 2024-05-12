from Image import Image
from PCAClass import PCAClass
from DatasetClass import DatasetClass
from imageToMatrixClass import ImageToMatrixClass
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np
import cv2
import io


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
        self.original_names = []
        self.finded_names = []
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

        if self.no_button_clicks == 0:
            self.action_button.setText('Next')

        if (self.no_button_clicks == len(self.imgs_paths_testing)-1):
            self.action_button.hide()
            self.label.setText(f"Total correct {self.correct}")
            self.person_label.setText(f"Total wrong {self.wrong}")
            self.percentage_label.setText(
                f"Percentage {round(self.correct / (self.correct + self.wrong) * 100,2)} %")
            roc_curve = self.plot_roc_curve(
                self.original_names, self.finded_names)
            self.display_image(roc_curve)
        else:
            img = self.PCAClass_obj.image_from_path(
                self.imgs_paths_testing[self.no_button_clicks])
            self.display_image(img)
            new_coords_for_img = self.PCAClass_obj.new_coord(img)

            finded_name = self.PCAClass_obj.recognize_face(new_coords_for_img)
            self.finded_names.append(finded_name)
            target_index = self.labels_imgs_testing[self.no_button_clicks]
            original_name = self.images_targets[target_index]
            self.original_names.append(original_name)

            if finded_name is original_name:
                self.correct += 1
                self.label.setText(f"correct Result, Name: {finded_name}")

            else:
                self.wrong += 1
                self.label.setText(f"wrong Result, Name: {finded_name}")

        self.no_button_clicks += 1

    def plot_roc_curve(self, y_true, y_score):
        # Binarize the labels
        classes = np.unique(y_true)
        n_classes = len(classes)
        y_true_binary = label_binarize(y_true, classes=classes)
        y_score_binary = label_binarize(y_score, classes=classes)

        # Compute ROC curve and ROC area for each class
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(
                y_true_binary[:, i], y_score_binary[:, i])
            roc_auc[i] = auc(fpr[i], tpr[i])

        # Plot ROC curve for each class
        plt.figure()
        plt.figure(figsize=(20, 10))
        for i in range(n_classes):
            plt.plot(fpr[i], tpr[i], lw=2, label='ROC curve (area = %0.2f) for class %s' % (
                roc_auc[i], classes[i]))
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic')
        plt.legend(loc="lower right")

        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        img_array = np.frombuffer(img_buffer.getvalue(), dtype=np.uint8)
        img_buffer.close()
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        return img
