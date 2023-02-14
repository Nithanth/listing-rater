import operator
import traceback
import numpy as np
from collections import defaultdict
import cv2
from brisque import BRISQUE


"""
Scrap code. Just mess around with it to test out the different functions. Final versions will be put
inside the class. 
"""
# url1 = 'https://www.airbnb.com/rooms/plus/24631451?adults=1&category_tag=Tag%3A8528&children=0&infants=0&search_mode=flex_destinations_search&check_in=2022-12-31&check_out=2023-01-05&federated_search_id=dc929bbc-6258-4540-8ab6-10c4b8ae8d07&source_impression_id=p3_1667267239_%2BwBRZPznhyu3hCd1'
img = cv2.imread('/Users/balurs/Documents/GitHub/listing-rater-frontend/backend/files/checks/image/images_to_test/dullness/notDull/NotDull_img1.png', cv2.IMREAD_COLOR)
# payload_str = payload[0]['src'].split(',')[1]
# decoded = decode_image(payload_str)
# print(type(decoded))
# np_array = np.frombuffer(decoded, np.uint8)
# img = cv2.imdecode(np_array, cv2.IMREAD_COLOR) 
# img = cv2.imread(np_array, cv2.IMREAD_COLOR)
# brisque score 
img_eval = BRISQUE(url=False)
print(img_eval.score(img))

# # blurryness score
# loaded_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# score = cv2.Laplacian(loaded_image, cv2.CV_64F).var()
# print(score)

# # dullness and whiteness score
# def color_analysis(img):
#     palatte = defaultdict(int)
#     height, width = img.shape[:2]
#     for i in range(height):
#         for j in range(width):
#             (b,g,r) = img[i,j]
#             palatte[(b,g,r)] += 1

#     # sort the colors present in the image 
#     sorted_x = sorted(palatte.items(), key=operator.itemgetter(1), reverse = True)
#     light_shade, dark_shade, shade_count, pixel_limit = 0, 0, 0, 25
#     for i, x in enumerate(sorted_x[:pixel_limit]):
#         if all(xx <= 20 for xx in x[0][:3]): ## dull : too much darkness 
#             dark_shade += x[1]
#         if all(xx >= 240 for xx in x[0][:3]): ## bright : too much whiteness 
#             light_shade += x[1]
#         shade_count += x[1]
        
#     light_percent = round((float(light_shade)/shade_count)*100, 2)
#     dark_percent = round((float(dark_shade)/shade_count)*100, 2)
#     return light_percent, dark_percent

# height, width = img.shape[:2]
# halves = (height//2, width//2)
# # im1 = im.crop((0, 0, width, halves[0]))
# im1 = img[0:halves[0], 0:halves[1]]
# # im2 = im.crop((0, halves[0], width, height))
# im2 = img[halves[0]:height, halves[1]:width]

# try:
#     light_percent1, dark_percent1 = color_analysis(im1)
#     light_percent2, dark_percent2 = color_analysis(im2)
# except Exception as e:
#     print(traceback.format_exc())

# light_percent = (light_percent1 + light_percent2)/2 
# dark_percent = (dark_percent1 + dark_percent2)/2 
# print(light_percent, dark_percent)


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
        loaded_image = cv2.imread(image)
        brisque_score = self.brisque_evaluator.score(loaded_image)
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
        self.image_score_data[image_id]["BRIQSUE score"] = brisque_score
        if brisque_score >= 60:
            self.image_score_data[image_id]["BRISQUE quality check"] = "good"
        else:
            self.image_score_data[image_id]["BRISQUE quality check"] = "bad"


    def resolution(self, image):
        loaded_image = cv2.imread(image)
        height, width = loaded_image.shape[:2]
        return (height, width)
    
    def resolution_eval(self, image_id, image):
        height, width = self.resolution(image)
        self.image_score_data[image_id]["resolution"] = (height, width)
        # AirBnB standards -> check if aspect ratio needs to be maintained also
        if width >= 1024 and height >= 683 and (width/height)==3/2:
            self.image_score_data[image_id]["resolution check"] = "sufficient"
        else:
            self.image_score_data[image_id]["resolution check"] = "insufficient"


    def blurriness_score(self, image):
        loaded_image = cv2.imread(image)
        gray_image = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)
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
        else:
            self.image_score_data[image_id]["blurriness quality check"] = "not blurry"
                
    
    def dullness_score(self, image):
        loaded_image = cv2.imread(image)
        # Convert the image to grayscale
        gray = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)
        
        # Convert the image to the CIELAB color space
        lab = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2LAB)
        
        # Split the image into the L, A, and B channels
        l_channel, a_channel, b_channel = cv2.split(lab)
        
        # Calculate the mean and standard deviation of the pixel intensities in the grayscale and color channels
        mean_gray_intensity = np.mean(gray)
        std_gray_intensity = np.std(gray)
        mean_a_intensity = np.mean(a_channel)
        mean_b_intensity = np.mean(b_channel)
        std_ab_intensity = np.sqrt(np.square(np.std(a_channel)) + np.square(np.std(b_channel)))
        
        # Calculate the dullness score as a combination of mean intensity, contrast, and colorfulness
        dullness_score = 255 - mean_gray_intensity + std_gray_intensity + 0.5 * (mean_a_intensity + mean_b_intensity) + 0.5 * std_ab_intensity
        return dullness_score
    
    def dullness_eval(self, image_id, image):
        dullness_score = self.dullness_score(image)
        self.image_score_data[image_id]["dullness score"] = dullness_score
        # threshold 400
        if dullness_score >= 400:
            self.image_score_data[image_id]["dullness quality check"] = "dull"
        else:
            self.image_score_data[image_id]["dullness quality check"] = "not dull"
    
    def image_checks(self):
        for image_id in self.image_score_data:
            try:
                image = self.image_score_data[image_id]
                self.brisque_eval(image_id, image)
                self.resolution_eval(image_id, image)
                self.blurriness_eval(image_id, image)
                self.dullness_eval(image_id, image)
            except:
                print(traceback.format_exc())

        return self.image_score_data
        
        

    



            

