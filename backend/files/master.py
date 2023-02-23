from checks.description import check_amenities
from checks.image.check_images import imageEvaluator
from checks.description.check_description import descriptionEvaluator
from checks.image import image_utils
import textgen_model
import traceback


def description_feedback(payload):
    description_evaluator = descriptionEvaluator(payload)
    description_evaluator.readability_check()
    description_evaluator.amenities_check()
    description_evaluator.nearby_attractions_check()
    return description_evaluator.description_data


def image_feedback(images):
    photobank = []
    for image_object in images:
        image_id = image_object["id"]
        raw_image_data = image_object["src"]
        photobank.append(
            (image_id, image_utils.convert_image_for_cv(raw_image_data)))
    image_evaluator = imageEvaluator(photobank)
    image_data = image_evaluator.image_checks()
    for image_id in image_data:
        try:
            raw_image_data = image_data[image_id]["raw image data"]
            image_data[image_id]["encoded image data"] = image_utils.convert_image_for_react(
                raw_image_data, format='.jpg')
            del image_data[image_id]["raw image data"]
        except TypeError:
            continue
        except:
            print(traceback.format_exc())
    return image_data


def generate_description(platform, address, amenities, bedroom_count, bathroom_count):
    if platform == "openai":
        response = textgen_model.generate_property_description_openai(
            address, amenities, bedroom_count, bathroom_count)
    elif platform == "cohere":
        response = textgen_model.generate_property_description_cohere(
            address, amenities, bedroom_count, bathroom_count)
    return response


description = """
Stylish, modern, and chic, two-bedroom, two bath home located on the border of the SOMA, Mission, and Hayes Valley district!
The unit has a contemporary and inviting floor plan characterized with gorgeous wood floors, gourmet kitchen with stainless steel appliances,
a comfortable living/dining area, and two significant bedrooms with plenty of natural light and are separated for privacy. Both bedrooms are
spacious and complete with ample closet space, access to private decks that overlook the garden-like outdoor space, and there is a laundry closet
for convenience. There is also an updated gym, common courtyard, grilling area, deeded storage, and available garage parking. Don't miss this wonderful
home that is close to shopping, world renowned dining, cafes, public transportation, tech shuttles, HWY 101/280 and more!
"""
description_more_sentences = """
Stylish, modern, and chic, two-bedroom, two bath home located on the border of the SOMA, Mission, and Hayes Valley district!
The unit has a contemporary and inviting floor plan with gorgeous wood floors, gourmet kitchen with stainless steel appliances,
a comfortable living/dining area, and two significant bedrooms. Plenty of natural light and are separated for privacy. Both bedrooms are
spacious. They are complete with ample closet space. They have access to private decks that overlook the garden-like outdoor space. There is a laundry closet
for convenience. There is also an updated gym, common courtyard, grilling area, deeded storage, and available garage parking. Don't miss this wonderful
home that is close to shopping, world renowned dining, cafes, public transportation, tech shuttles, HWY 101/280 and more!
"""

description_shorter_words = """
Stylish, modern, and chic, two-bedroom, two bath home located on the border of the SOMA, Mission, and Hayes Valley district!
The unit has a contemporary floor plan with gorgeous wood floors, stainless steel appliances, and two significant bedrooms with plenty of natural light and are separated for privacy. Both bedrooms are
spacious and complete with  closet space, access to private decks that overlook the garden and gorgeous pool, and there is a laundry closet
for convenience. There is also an updated gym, common courtyard, grilling area, deeded storage, and available garage parking. Don't miss this wonderful
home that is close to shopping, world renowned dining, cafes, public transportation, tech shuttles, HWY 101/280 and more!
"""

description_test = """
The fox jumped over the cliff.
"""

# checkForNearbyAmenities(description)
# checkForNearbyAmenities(description1)
# cases = []
# cases.append(description)
# cases.append(description_more_sentences)
# cases.append(description_shorter_words)
# cases.append(description_test)
# for x in cases:
#     print(description_feedback(x))
