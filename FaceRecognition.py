# from DatasetClass import DatasetClass
# # from imageToMatrixClass import ImageToMatrixClass
# from PCAClass import PCAClass
# import cv2

# reco_type = "group"
# num_of_imgs_for_person = 8
# dataset_obj = DatasetClass(num_of_imgs_for_person)

# imgs_paths_training = dataset_obj.images_path_training
# labels_imgs_training = dataset_obj.labels_for_training
# num_of_elements_training = dataset_obj.num_of_images_training


# imgs_paths_testing = dataset_obj.images_path_testing
# labels_imgs_testing = dataset_obj.labels_for_testing
# num_of_elements_testing = dataset_obj.num_of_images_testing

# images_targets = dataset_obj.images_target

# img_width, img_height = 50, 50
# # ImageToMatrixClass_obj = ImageToMatrixClass(
# #     imgs_paths_training, img_height, img_width)

# img_matrix = ImageToMatrixClass_obj.get_matrix()

# PCAClass_obj = PCAClass(img_matrix, labels_imgs_training, images_targets,
#                         img_height, img_width, num_of_elements_training, quality_percent=90)

# new_coord = PCAClass_obj.reduce_dim()

# if reco_type == "image":
#     correct = 0
#     wrong = 0
#     i = 0

#     for img_path in imgs_paths_testing:
#         img = PCAClass_obj.image_from_path(img_path)
#         PCAClass_obj.show_image("Recognize Image", img)
#         new_coords_for_img = PCAClass_obj.new_coord(img)

#         finded_name = PCAClass_obj.recognize_face(new_coords_for_img)
#         target_index = labels_imgs_testing[i]
#         original_name = images_targets[target_index]

#         if finded_name is original_name:
#             correct += 1
#             print("Correct Result", "Name:", finded_name)

#         else:
#             wrong += 1
#             print("Wrong Result", "Name:", finded_name)
#         i += 1

#     print("Total Correct", correct)
#     print("Total Wrong", wrong)
#     print("Percentage", correct / (correct + wrong) * 100)

# # if reco_type == "group":
# #     face_cascade = cv2.CascadeClassifier(
# #         "cascaded\data\haarcascade_frontalface_alt2.xml")

# #     frame = cv2.imread(
# #         "GroupImages\group_image.jpg")

# #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# #     faces = face_cascade.detectMultiScale(
# #         gray, scaleFactor=1.5, minNeighbors=3)

# #     i = 0

# #     for (x, y, w, h) in faces:
# #         roi_gray = gray[y:y+h, x:x+w]
# #         scaled = cv2.resize(roi_gray, (img_height, img_width))
# #         rec_color = (0, 255, 0)
# #         rec_stroke = 2
# #         cv2.rectangle(frame, (x, y), (x+w, y+h), rec_color, rec_stroke)

# #         new_cord = PCAClass_obj.new_coord(scaled)
# #         name = PCAClass_obj.recognize_face(new_cord)
# #         font = cv2.FONT_HERSHEY_SIMPLEX
# #         font_color = (255, 0, 0)
# #         font_stroke = 2
# #         cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1,
# #                     font_color, font_stroke)
# #         print(name)
# #         i += 1

# #     frame = cv2.resize(frame, (1080, 568))
# #     cv2.imshow('Colored Frame', frame)
# #     cv2.waitKey()
