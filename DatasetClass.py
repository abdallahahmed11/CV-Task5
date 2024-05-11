import os


class DatasetClass:
    def __init__(self, training_num):
        dataset_path = "ORL"

        self.images_path_training = []
        self.labels_for_training = []
        self.num_of_images_training = []

        self.images_path_testing = []
        self.labels_for_testing = []
        self.num_of_images_testing = []

        self.images_target = []

        per_num = 0

        for person_name in os.listdir(dataset_path):
            person_name_path = os.path.join(dataset_path, person_name)
            if os.path.isdir(person_name_path):
                if len(os.listdir(person_name_path)) >= training_num:
                    i = 0
                    for image_name in os.listdir(person_name_path):
                        img_path = os.path.join(person_name_path, image_name)

                        if i < training_num:
                            self.images_path_training += [img_path]
                            self.labels_for_training += [per_num]

                            if len(self.num_of_images_training) > per_num:
                                self.num_of_images_training[per_num] += 1
                            else:
                                self.num_of_images_training += [1]

                            if i == 0:
                                self.images_target += [person_name]
                        else:
                            self.images_path_testing += [img_path]
                            self.labels_for_testing += [per_num]

                            if len(self.num_of_images_testing) > per_num:
                                self.num_of_images_testing[per_num] += 1
                            else:
                                self.num_of_images_testing += [1]
                        i += 1
                    per_num += 1
