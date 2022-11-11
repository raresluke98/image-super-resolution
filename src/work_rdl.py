from image_helper import ImageManager
from image_helper import downscale_image
import cv2


if True:
    image_manager = ImageManager(image_dir='images')
    image = image_manager.read_image(file_name='zebra.png')
    downscaled_image = downscale_image(input_image=image, scale=0.5)
