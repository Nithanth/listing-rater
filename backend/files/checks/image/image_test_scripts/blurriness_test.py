import cv2

def blurriness_score(image_filepath):
    image = cv2.imread(image_filepath)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply different kernel sizes to the Laplacian filter
    score_3 = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    score_5 = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=5).var()
    score_7 = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=7).var()
    # Take the average of the scores to improve accuracy
    score = (score_3 + score_5 + score_7) / 3
    # Apply a threshold to classify the photo as "blurry" or "sharp"
    threshold = 50
    if score < threshold:
        return "blurry"
    else:
        return "sharp"