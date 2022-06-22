import cv2
import cvlib as cv
import numpy as np


class DetecterGender:

    def __init__(self, padding=15):
        self.padding = padding
        self.path_save = None
        self.gender = None
        self.img = None
        self.faces = None
        self.conf = None

    def read_image(self, img: str) -> any:
        try:
            self.img = cv2.imread(f"detected_img/{img}")
        except Exception as err:
            return err

    def faces_detection(self):
        self.faces, self.conf = cv.detect_face(self.img)

    def faces_gender_detection(self):
        for face in self.faces:
            start_x = max(0, face[0] - self.padding)
            start_y = max(0, face[1] - self.padding)
            end_x = min(self.img.shape[1] - 1, face[2] + self.padding)
            end_y = min(self.img.shape[0] - 1, face[3] + self.padding)

            face_crop = np.copy(self.img[start_y:end_y, start_x:end_x])

            if self._detect_gender(face_crop):
                self._save_image(start_y, end_y, start_x, end_x)

    def _detect_gender(self, face):
        label, confidence = cv.detect_gender(face)
        idx = np.argmax(confidence)
        label = label[idx]

        if label == self.gender:
            return True

    def _save_image(self, start_y, end_y, start_x, end_x):
        print(f"{self.path_save}{start_y}{end_y}{start_x}{end_x}.jpg")
        cv2.imwrite(f"{self.path_save}{start_y}{end_y}{start_x}{end_x}.jpg", self.img[start_y:end_y, start_x:end_x])


class DetecterMale(DetecterGender):

    def __init__(self):
        super().__init__()
        self.path_save = "new_detected_img/masculino/"
        self.gender = "male"


class DetecterFemale(DetecterGender):

    def __init__(self):
        super().__init__()
        self.path_save = "new_detected_img/feminino/"
        self.gender = "female"









