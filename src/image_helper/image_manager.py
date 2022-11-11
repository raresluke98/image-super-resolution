"""Class for managing image reading/writing"""
import cv2
import numpy as np

class ImageManager:

    image_dir: str = None


    def __init__(self, image_dir: str):
        assert image_dir and isinstance(image_dir, str), \
            "Image dir cannot be None or empty string"

        if not image_dir.endswith('/'):
            image_dir += '/'

        self.image_dir = image_dir


    def read_image(self, file_name: str):
        """Read image from given path and return array"""
        image_path = self.image_dir + file_name
        image = cv2.imread(image_path)
        return image

    @staticmethod
    def get_image_size(image) -> np.ndarray:
        size = np.asarray(image.shape[:2], dtype='int')
        return size
