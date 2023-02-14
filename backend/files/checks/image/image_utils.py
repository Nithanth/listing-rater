import base64
import numpy as np
import cv2

def encode_image(image):
    return base64.b64encode(image)

def decode_image(image):
    return base64.b64decode(image)

def convert_image_for_cv(image):
    raw_image= image.split(',')[1]
    decoded = decode_image(raw_image)
    np_array = np.frombuffer(decoded, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR) 
    return image