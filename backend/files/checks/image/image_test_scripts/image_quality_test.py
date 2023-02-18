import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.color import rgb2gray
import tensorflow as tf
import tensorflow_hub as hub

def evaluate_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    # Calculate BRISQUE score
    brisque = cv2.quality.QualityBRISQUE_compute(img).getQualityBRISQUE()
    
    # Calculate sharpness using Laplacian variance
    lap_var = cv2.Laplacian(img, cv2.CV_64F).var()
    
    # Calculate color balance using standard deviation of RGB channels
    b, g, r = cv2.split(img)
    std_dev = np.std([np.mean(r), np.mean(g), np.mean(b)])
    
    # Calculate SSIM score
    gray = rgb2gray(img)
    ssim_score = ssim(gray, gray, data_range=gray.max() - gray.min())
    
    # Calculate image content factor
    # Use a pre-trained deep learning model to calculate the content score
    content_module_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/feature_vector/5"
    content_module = hub.load(content_module_url)
    resized_image = tf.image.resize(img, (224, 224))
    content_features = content_module(resized_image[np.newaxis, ...])
    content_score = content_features.numpy().mean()
    
    # Calculate distortion factor
    # Distortion score based on the difference between the vertical and horizontal edge lengths
    edges = cv2.Canny(img, 100, 200)
    h, w = img.shape[:2]
    v_edge_len = np.sum(edges[:h//2, :])
    h_edge_len = np.sum(edges[h//2:, :])
    distortion_score = abs(v_edge_len - h_edge_len) / (v_edge_len + h_edge_len)
    
    # Calculate lighting factor
    # Lighting score based on contrast and color temperature
    center = img[h//4:3*h//4, w//4:3*w//4]
    
    # Calculate contrast score using the standard deviation of the center of the image
    gray_center = cv2.cvtColor(center, cv2.COLOR_BGR2GRAY)
    contrast_score = np.std(gray_center)
    
    # Calculate color temperature using the difference between the mean R and B values
    mean_r = np.mean(center[:,:,2])
    mean_b = np.mean(center[:,:,0])
    color_temp_score = abs(mean_r - mean_b)
    
    # Calculate lighting score as a weighted average of contrast and color temperature scores
    lighting_score = 0.6 * (1 - contrast_score / 255) + 0.4 * (1 - color_temp_score / 255)
    # Define subscore thresholds
    ssim_threshold = 0.75
    lap_var_threshold = 50
    std_dev_threshold = 40
    brisque_threshold = 50
    content_threshold = 0.1
    distortion_threshold = 0.5
    lighting_threshold = 0.6
    
    # Classify image quality based on subscores
    subscores = [ssim_score, lap_var, std_dev, brisque, content_score, distortion_score, lighting_score]
    thresholds = [ssim_threshold, lap_var_threshold, std_dev_threshold, brisque_threshold, content_threshold, distortion_threshold, lighting_threshold]
    subscore_results = ["good quality" if subscore >= threshold else "bad quality" for subscore, threshold in zip(subscores, thresholds)]
    
    # Combine the scores into a single metric
    score = 0.2 * (1 - ssim_score) + 0.3 * (1 - lap_var/10000) + 0.1 * std_dev + 0.2 * brisque + 0.15 * content_score + 0.05 * distortion_score + 0.1 * lighting_score
    return score, all(x == 'good quality' for x in subscore_results), "good score" if score>0.6 else "bad score"