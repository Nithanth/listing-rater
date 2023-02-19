import cv2
import os
import pandas as pd
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
        return "blurry", score
    else:
        return "sharp", score

image_data = []

# assign directory
directories = ['images_to_test/blurriness/blurry', 'images_to_test/blurriness/crisp']
 
# iterate over files in
# that directory
for directory in directories:
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            split_path = f.copy().split('/')
            id, true_label = split_path[-1], split_path[-2]
            output_label, score = blurriness_score(f)
            image_data.append({'unique_id': id, 'true_label': true_label, 'score': score, 'output_label': output_label})

df = pd.DataFrame(image_data)
print(df)





        