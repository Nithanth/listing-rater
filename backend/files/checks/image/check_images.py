from email.encoders import encode_base64
import os 
import operator
import traceback
import numpy as np
from collections import defaultdict
import cv2
from brisque import BRISQUE
from utilities import decode_image


"""
Scrap code. Just mess around with it to test out the different functions. Final versions will be put
inside the class. 
"""
# url1 = 'https://www.airbnb.com/rooms/plus/24631451?adults=1&category_tag=Tag%3A8528&children=0&infants=0&search_mode=flex_destinations_search&check_in=2022-12-31&check_out=2023-01-05&federated_search_id=dc929bbc-6258-4540-8ab6-10c4b8ae8d07&source_impression_id=p3_1667267239_%2BwBRZPznhyu3hCd1'
img = cv2.imread('/Users/nithanth/Angel/airbnb-work/api/checks/airbnb_test.png', cv2.IMREAD_COLOR)
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
Whiteness Score - How white an image is - threshold yet to be determined through trial
Resolution - Dimensions of image matched to Airbnb standards
"""
class imageEvaluator:
    def __init__(self, images):
        self.image_list = images
        self.brisque_evaluator = BRISQUE(url=False)
        self.image_score_data = defaultdict(dict)
    
    def add_image(self, image):
        self.image_score_data[image] = {}

    def remove_image(self, image):
        if image in self.image_score_data:
            self.image_score_data.pop(image)
            return f"{image} has been removed"
        else:
            return f"{image} not found"

    def clear_data(self):
        self.image_score_data.clear()
    
    def brisque_score(self, image):
        loaded_image = cv2.imread(image)
        brisque_score = self.brisque_evaluator.score(loaded_image)
        self.image_score_data[image]["BRISQUE score"] = brisque_score

    def brisque_avg(self):
        avg = 0
        try:
            for image in self.image_score_data:
                avg += image["BRISQUE score"]
            return (avg/len(self.image_score_data))        
        except:
            return "image data not populated"
    
    def brisque_eval(self, image):
        pass

    def resolution(self, image):
        loaded_image = cv2.imread(image)
        height, width = loaded_image.shape[:2]
        self.image_score_data[image]["resolution"] = (height, width)
    
    def resolution_eval(self, image):
        pass

    # apply the laplacian filter to the image and take the variance in order to determine bluryness score
    def blurrness_score(self, image):
        loaded_image = cv2.imread(image)
        loaded_image = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)
        score = cv2.Laplacian(loaded_image, cv2.CV_64F).var()
        self.image_score_data[image]["blurness score"] = score
    
    def blurrness_avg(self):
        avg = 0
        try:
            for image in self.image_score_data:
                avg += image["blurness score"]
            return (avg/len(self.image_score_data))        
        except:
            print(traceback.format_exc())
            return "image data not populated"
    
    def blurrrness_eval(self, image):
        pass
    
    
    def dullness_whiteness_scores(self, image):
        height, width = image.shape[:2]
        halves = (height//2, width//2)
        image1 = image[0:halves[0], 0:halves[1]]
        image2 = image[halves[0]:height, halves[1]:width]

        def color_analysis(image, height, width):
            palatte = defaultdict(int)
            height, width = image.shape[:2]
            for i in range(height):
                for j in range(width):
                    (b,g,r) = image[i,j]
                    palatte[(b,g,r)] += 1

            # sort the colors present in the image 
            sorted_palette = sorted(palatte.items(), key=operator.itemgetter(1), reverse = True)
            light_shade, dark_shade, shade_count, pixel_limit = 0, 0, 0, 25
            for i, x in enumerate(sorted_palette[:pixel_limit]):
                if all(xx <= 20 for xx in x[0][:3]): ## dull : too much darkness 
                    dark_shade += x[1]
                if all(xx >= 240 for xx in x[0][:3]): ## bright : too much whiteness 
                    light_shade += x[1]
                shade_count += x[1]
            
            # calculate percent of the shade that is light and dark based on the total shade count
            light_percent = round((float(light_shade)/shade_count)*100, 2)
            dark_percent = round((float(dark_shade)/shade_count)*100, 2)
            return light_percent, dark_percent

        try:
            light_percent1, dark_percent1 = color_analysis(image1)
            light_percent2, dark_percent2 = color_analysis(image2)
        except:
            print(traceback.format_exc())

        light_percent = (light_percent1 + light_percent2)/2 
        dark_percent = (dark_percent1 + dark_percent2)/2 
        return light_percent, dark_percent
    
    def dullness_whiteness_eval(self, image):
        pass
        
        

    



            

