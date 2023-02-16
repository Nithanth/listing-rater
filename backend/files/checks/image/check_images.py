import operator
import traceback
import numpy as np
from collections import defaultdict
import cv2
from brisque import BRISQUE

"""
This class contains all the functionality to evaluate a user's images. Metrics used to evaluate images 
include...
BRISQUE Score - Non-referential subjective image quality score scaled from 0-100 (with 0 being the best)
Blurryness Score - How blurry an image is - threshold yet to be determined through trial 
Dullness Score - How dull an image is - threshold yet to be determined through trial
Whiteness Score - How white an image is - threshold yet to be determined through trial - TBD
Resolution - Dimensions of image matched to Airbnb standards
"""
class imageEvaluator:
    def __init__(self, images):
        self.brisque_evaluator = BRISQUE(url=False)
        self.image_score_data = defaultdict(dict)
        for image_id, image in images:
            self.image_score_data[image_id]["raw image data"] = image # raw image data base64 decoded pre-openCV read
            self.image_score_data[image_id]["image id"] = image_id
        self.image_score_data["dull images"] = list()
        self.image_score_data["blurry images"] = list()
        self.image_score_data["high BRISQUE images"] = list()
        self.image_score_data["bad resolution images"] = list()
    
    def add_image(self, image_id, image):
        self.image_score_data[image_id]["raw image data"] = image

    def remove_image(self, image_id):
        if image_id in self.image_score_data:
            self.image_score_data.pop(image_id)
            return f"{image_id} has been removed"
        else:
            return f"{image_id} not found"

    def clear_data(self):
        self.image_score_data.clear()
    
    def brisque_score(self, image):
        brisque_score = self.brisque_evaluator.score(image)
        return brisque_score

    def brisque_avg(self):
        avg = 0
        try:
            for image in self.image_score_data:
                avg += self.image_score_data[image]["BRISQUE score"]
            return (avg/len(self.image_score_data))        
        except:
            print(traceback.format_exc())
            return "image data not populated"
    
    def brisque_eval(self, image_id, image):
        brisque_score = self.brisque_score(image)
        # threshold 60
        self.image_score_data[image_id]["BRISQUE score"] = brisque_score
        if brisque_score <= 60:
            self.image_score_data[image_id]["BRISQUE quality check"] = "good"
            return False
        else:
            self.image_score_data[image_id]["BRISQUE quality check"] = "bad"
            return True


    def resolution(self, image):
        height, width = image.shape[:2]
        return (height, width)
    
    def resolution_eval(self, image_id, image):
        height, width = self.resolution(image)
        self.image_score_data[image_id]["resolution"] = (height, width)
        # AirBnB standards -> check if aspect ratio needs to be maintained also
        if width >= 1024 and height >= 683 and (width/height)==3/2:
            self.image_score_data[image_id]["resolution check"] = "sufficient"
            return False
        else:
            self.image_score_data[image_id]["resolution check"] = "insufficient"
            return True


    def blurriness_score(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # apply the laplacian filter to the image and take the variance in order to determine bluryness score
        score = cv2.Laplacian(gray_image, cv2.CV_64F).var()
        return score
        # self.image_score_data[image_id]["blurriness score"] = score
    
    def blurriness_avg(self):
        avg = 0
        try:
            for image in self.image_score_data:
                avg += self.image_score_data[image]["blurriness score"]
            return (avg/len(self.image_score_data))        
        except:
            print(traceback.format_exc())
            return "image data not populated"
    
    def blurriness_eval(self, image_id, image):
        blurriness_score = self.blurriness_score(image)
        self.image_score_data[image_id]["blurriness score"] = blurriness_score
        # threshold 1000
        if blurriness_score < 1000:
            self.image_score_data[image_id]["blurriness quality check"] = "blurry"
            return True
        else:
            self.image_score_data[image_id]["blurriness quality check"] = "not blurry"
            return False
                
    
    def dullness_score(self, image):
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
        return dullness_score
    
    def dullness_eval(self, image_id, image):
        dullness_score = self.dullness_score(image)
        self.image_score_data[image_id]["dullness score"] = dullness_score
        # threshold 100
        if dullness_score >= 100:
            self.image_score_data[image_id]["dullness quality check"] = "dull"
            return True
        else:
            self.image_score_data[image_id]["dullness quality check"] = "not dull"
            return False
    
    def image_checks(self):
        for image_id in self.image_score_data:
                try:
                    image = self.image_score_data[image_id]["raw image data"]
                    if self.brisque_eval(image_id, image):
                        self.image_score_data["high BRISQUE images"].append(image_id)
                    if self.resolution_eval(image_id, image):
                        self.image_score_data["bad resolution images"].append(image_id)
                    if self.blurriness_eval(image_id, image):
                        self.image_score_data["blurry images"].append(image_id)
                    if self.dullness_eval(image_id, image):
                        self.image_score_data["dull images"].append(image_id)
                except TypeError:
                    print(f"Skipping image {image_id}: TypeError")
                    continue
                except ValueError:
                    print(f"image {image_id}: ValueError")
                    print(traceback.format_exc())
                except Exception as e:
                    print(f"image {image_id}: {e}")
                    print(traceback.format_exc())

        return self.image_score_data
        
        

    



            

