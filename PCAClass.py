import scipy.linalg as s_linalg
import cv2
import numpy as np


class PCAClass:
    def __init__(self, image_matrix, image_lables, image_targets, image_height, image_width, no_of_elements, quality_percent):
        self.image_matrix = image_matrix
        self.image_lables = image_lables
        self.image_targets = image_targets
        self.image_height = image_height
        self.image_width = image_width
        self.no_of_elements = no_of_elements
        self.quality_percent = quality_percent

        mean = np.mean(self.image_matrix, 1)
        self.mean_face = np.asmatrix(mean).T

        self.image_matrix -= self.mean_face

    def give_p_value(self, eig_values):
        sum_eig_values = np.sum(eig_values)
        sum_threshold = sum_eig_values * self.quality_percent / 100
        sum_temp = 0
        p = 0

        while sum_temp < sum_threshold:
            sum_temp += eig_values[p]
            p += 1

        return p

    def reduce_dim(self):
        u, eig_values, v_t = s_linalg.svd(
            self.image_matrix, full_matrices=True)
        p = self.give_p_value(eig_values)
        self.new_basis = u[:, 0:p]
        self.new_coordinates = np.dot(self.new_basis.T, self.image_matrix)
        return self.new_coordinates

    def new_coord(self, single_img):
        img_vec = np.asmatrix(single_img).ravel()
        img_vec = img_vec.T

        new_mean = ((self.mean_face * len(self.image_lables)) +
                    img_vec) / (len(self.image_lables) + 1)

        img_vec = img_vec - new_mean

        return np.dot(self.new_basis.T, img_vec)

    def recognize_face(self, new_coords_of_image):
        classes = len(self.no_of_elements)
        dist = []
        start = 0

        for i in range(classes):
            temp_imgs = self.new_coordinates[:, int(
                start):int(start + self.no_of_elements[i])]
            mean_temp = np.asmatrix(np.mean(temp_imgs, 1)).T
            start = start + self.no_of_elements[i]
            dist_temp = np.linalg.norm(new_coords_of_image - mean_temp)
            dist += [dist_temp]

        min_pos = np.argmin(dist)
        return self.image_targets[min_pos]

    def image_from_path(self, path):
        gray = cv2.imread(path, 0)
        return cv2.resize(
            gray, (self.image_width, self.image_height))

    def new_to_old_cord(self, new_cords):
        return self.mean_face + (np.asmatrix(np.dot(self.new_basis, new_cords))).T

    def show_image(self, label_to_show, old_cords):
        old_cords_matrix = np.reshape(
            old_cords, [self.image_width, self.image_height])

        old_cords_integers = np.array(old_cords_matrix, dtype=np.uint8)

        resized_img = cv2.resize(old_cords_integers, (500, 500))

        cv2.imshow(label_to_show, resized_img)
        cv2.waitKey()

    def show_eigen_faces(self, min_pix_int, max_pix_int, eig_face_no):
        ev = self.new_basis[:, eig_face_no:eig_face_no+1]
        min_orig = np.min(ev)
        max_orig = np.max(ev)

        ev = min_pix_int + \
            (((max_pix_int-min_pix_int)/(max_orig-min_orig)) * ev)

        self.show_image("eigen face" + str(eig_face_no), ev)
