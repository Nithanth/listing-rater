from checks.description import check_amenities
from checks.image.check_images import imageEvaluator
from checks.image import image_utils
import textgen_model
import traceback

def checkForNearbyAmenities(description):
    result = check_amenities.amenitiesNearby(description)

    if result[0] == False:
        # No nearby amenities found
        print('''To increase bookings, consider including nearby amenities! This will give guests a better understanding of the area and will help you increase 
        your occupancy rate''')
    else:
        if result[1] == False:
            print('''We noticed you listed nearby amenities, but didn't include the relative distances.
            Showing guests how close amenities are to your property will make them feel more comfortable and help you increase bookings!''')
        else:
            print('''Good job on listing nearby amenities and relative distances! You rock!''')
# this file should call all check functions and based on what they return, recommend feedback to user

# call amenities here and return this feedback based on that
    # function should return feedback to user
    # case 1: good! proper nouns identified and proximity (time or distance) mentioned
    # case 2: you can be more descriptive! proper nouns identified, but can't identify any quantitative indication of proximity
    # case 3: bad! not enough proper nouns identified

def description_feedback(payload):
    pass

def image_feedback(images):
    photobank = []
    for image_object in images:
        image_id = image_object["id"]
        raw_image_data = image_object["src"]
        photobank.append((image_id, image_utils.convert_image_for_cv(raw_image_data)))
    image_evaluator = imageEvaluator(photobank) 
    image_data = image_evaluator.image_checks()
    for image_id in image_data:
        try:
            raw_image_data = image_data[image_id]["raw image data"]
            image_data[image_id]["encoded image data"] = image_utils.convert_image_for_react(raw_image_data, format='.jpg')
            del image_data[image_id]["raw image data"]
        except TypeError:
            continue
        except:
            print(traceback.format_exc())
    return image_data

def generate_description(platform, address):
    if platform == "openai":
        response = textgen_model.generate_property_description_openai(address)
    elif platform == "cohere":
        response = textgen_model.generate_property_description_cohere(address)
    return response

description = """
Stylish, modern, and chic, two-bedroom, two bath home located on the border of the SOMA, Mission, and Hayes Valley district!
The unit has a contemporary and inviting floor plan characterized with gorgeous wood floors, gourmet kitchen with stainless steel appliances,
a comfortable living/dining area, and two significant bedrooms with plenty of natural light and are separated for privacy. Both bedrooms are
spacious and complete with ample closet space, access to private decks that overlook the garden-like outdoor space, and there is a laundry closet
for convenience. There is also an updated gym, common courtyard, grilling area, deeded storage, and available garage parking. Don't miss this wonderful
home that is close to shopping, world renowned dining, cafes, public transportation, tech shuttles, HWY 101/280 and more!
"""

description1 = """
Stylish, modern, and chic, two-bedroom, two bath home located on the border of the SOMA, Mission, and Hayes Valley district! The property is 3 blocks away
from Papa's Pizzeria and 2 minutes away from Thailand. The unit has a contemporary and inviting floor plan characterized with gorgeous wood floors, gourmet
kitchen with stainless steel appliances, a comfortable living/dining area, and two significant bedrooms with plenty of natural light and are separated for privacy.
Both bedrooms are spacious and complete with ample closet space, access to private decks that overlook the garden-like outdoor space, and there is a laundry closet
for convenience. HEB is also 3 min away and a Kroger's is 2 miles down the road. There is also an updated gym, common courtyard, grilling area, deeded storage, and available garage parking. Don't miss this wonderful
home that is close to shopping, world renowned dining, cafes, public transportation, tech shuttles, HWY 101/280 and more!
"""

# checkForNearbyAmenities(description)
# checkForNearbyAmenities(description1)
