import cv2
import numpy as np
import os
import pandas as pd
def dullness_score(image_filepath):
        image = cv2.imread(image_filepath)
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Convert the image to the CIELAB color space
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        
        # Split the image into the L, A, and B channels
        l_channel, a_channel, b_channel = cv2.split(lab)
        
        # Calculate the mean and standard deviation of the pixel intensities in the grayscale and color channels
        mean_gray_intensity = np.mean(gray)
        std_gray_intensity = np.std(gray)
        mean_a_intensity = np.mean(a_channel)
        mean_b_intensity = np.mean(b_channel)
        std_ab_intensity = np.sqrt(np.square(np.std(a_channel)) + np.square(np.std(b_channel)))
        
        # Calculate the dullness score as a combination of mean intensity, contrast, and colorfulness
        dullness_score = 255 - mean_gray_intensity + 0.8 * std_gray_intensity + 0.4 * (mean_a_intensity + mean_b_intensity) + 1.2 * std_ab_intensity
        threshold = 100
        return (dullness_score, "not dull") if dullness_score < threshold else (dullness_score, "dull")
    

image_data = []
# assign directory
directories = ['images_to_test/dullness/dull', 'images_to_test/dullness/notDull']
 
# iterate over files in
# that directory
for directory in directories:
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            split_path = f.copy().split('/')
            id, true_label = split_path[-1], split_path[-2]
            score, output_label = dullness_score(f)
            image_data.append({'unique_id': id, 'true_label': true_label, 'score': score, 'output_label': output_label})

df = pd.DataFrame(image_data)
print(df)