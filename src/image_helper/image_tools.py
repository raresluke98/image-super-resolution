from ctypes import resize
import cv2
import numpy as np
from image_helper import ImageManager


def show_image(image):
    """Show image using cv2; close window by pressing any key"""
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows


def downscale_image(input_image: np.ndarray, scale: float, interpolation=cv2.INTER_LINEAR):
    """Downscale image by given scale factor using custom interpolation function"""
    assert 0.0 < scale <= 1.0, f"'scale={scale}' not in (0, 1)"
    input_image_size = ImageManager.get_image_size(image=input_image)
    resized_image_size = np.floor(input_image_size * scale).astype('int')
    resized_image = cv2.resize(input_image, resized_image_size, interpolation=interpolation)
    return resized_image
