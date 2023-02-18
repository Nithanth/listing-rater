import cv2

def is_airbnb_photo_valid(photo_path):
    # Read the photo using OpenCV
    photo = cv2.imread(photo_path)
    if photo is None:
        return False

    # Check the photo resolution
    height, width, channels = photo.shape
    if height < 683 or width < 1024:
        return False

    # Check the photo aspect ratio
    aspect_ratio = width / height
    if abs(aspect_ratio - 3/2) > 0.1:
        return False
    return True