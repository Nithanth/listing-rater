import base64
import numpy as np
import cv2

def encode_image(image):
    return base64.b64encode(image)

def decode_image(image):
    return base64.b64decode(image)

def convert_image_for_cv(image):
    try:
        if not isinstance(image, str):
            raise ValueError("Input image must be a string")
        if not image.startswith('data:image'):
            raise ValueError("Input image is not a valid base64 encoded image")
        
        raw_image = image.split(',')[1]
        decoded = decode_image(raw_image)
        np_array = np.frombuffer(decoded, np.uint8)
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError("Unable to decode image")
        
        return image
    except Exception as e:
        print(f"Error converting image: {str(e)}")
        return None

def convert_image_for_react(image, format):
    try:
        _, buffer = cv2.imencode(format, image)
    except cv2.error as e:
        # Handle encoding error
        print(f"Error: {e}")
        return None
    try:
        image_as_text = encode_image(buffer).decode('utf-8')
        return f"data:image;base64,{image_as_text}"
    except base64.binascii.Error as e:
        # Handle base64 encoding error
        print(f"Error: {e}")
        return None


