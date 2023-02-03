import base64

def encode_image(image):
    return base64.b64encode(image)

def decode_image(image):
    return base64.b64decode(image)