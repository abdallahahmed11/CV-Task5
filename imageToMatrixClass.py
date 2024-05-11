import scipy
import cv2 as cv
import numpy as np


class ImageToMatrixClass:
    def __init__(self, images_paths, image_height, image_width):
        self.images_paths = images_paths
        self.images_width = image_width
        self.images_height = image_height
        self.images_size = image_width * image_height

    def get_matrix(self):
        col = len(self.images_paths)

        image_matrix = np.zeros((self.images_size, col))
        i = 0
        for path in self.images_paths:
            gray = cv.imread(path, 0)
            gray_resized = cv.resize(
                gray, (self.images_width, self.images_height))

            mat_gray = np.asmatrix(gray_resized)
            vector = mat_gray.ravel()

            image_matrix[:, i] = vector
            i += 1

        return image_matrix 
