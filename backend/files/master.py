from checks.description import check_amenities
from checks.image.check_images import imageEvaluator
import utilities

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

def checkImages(payload):
    images = payload["images"]
    photobank = []
    for image in images:
        photobank.append(utilities.decode_image(image))
    evaluator = imageEvaluator(images)

    pass

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
checkForNearbyAmenities(description1)
