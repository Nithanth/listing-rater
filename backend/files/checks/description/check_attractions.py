import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from collections import Counter

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

# Scan description for proper nouns to see if host listed restaurants / attractions in the area and rough distance estimates
# If can't find distances, add a recommendation to user


def find_nearby_attractions(description):

    # look around current word index within 10 words for any quantitative indication of distances
    # check for "minute", "min", "hour", "hour", "hr" "mi", "miles"
    def find_proximity_indicators(tokens, idx):
        proximityIndicators = ['minute', 'min', 'mins', 'minutes',
                               'hour', 'hours', 'hr', 'mi', 'mile', 'miles', 'block', 'blocks']

        start = min(0, idx-10)
        end = min(len(tokens), idx+10)
        tokens = tokens[start:end]
        for token in tokens:
            target = token.replace('.', '')
            target = token.replace(',', '')
            target = token.replace('!', '')
            if target in proximityIndicators:
                return True

        return False

    # tokens is array containing each word / punctuation in separate index
    tokens = nltk.word_tokenize(description)
    tags = nltk.pos_tag(tokens)
    counts = Counter(tag for word,  tag in tags)

    singular, plural = counts['NNP'], counts['NNPS']
    proper_nouns = singular + plural

    # following result will be returned to masterchecks
    # if result[0] is True, user was specific mentioned amenities
    # if result[1] is True, that means user informed guests of distances to amenities well
    result = [False, False]

    # make better condition for this later
    if proper_nouns > 7:
        result[0] = True

    denom = 0.0
    count = 0.0
    for idx, word in enumerate(tags):
        if word[1] == 'NNP' or word[1] == 'NNPS':
            denom += 1.0
            if find_proximity_indicators(tokens, idx):
                count += 1.0
    if denom > 0 and count / denom > .5:
        result[1] = True

    return result


# test with following
#
# description = """
# Stylish, modern, and chic, two-bedroom, two bath home located on the border of the SOMA, Mission, and Hayes Valley district!
# The unit has a contemporary and inviting floor plan characterized with gorgeous wood floors, gourmet kitchen with stainless steel appliances,
# a comfortable living/dining area, and two significant bedrooms with plenty of natural light and are separated for privacy. Both bedrooms are
# spacious and complete with ample closet space, access to private decks that overlook the garden-like outdoor space, and there is a laundry closet
# for convenience. There is also an updated gym, common courtyard, grilling area, deeded storage, and available garage parking. Don't miss this wonderful
# home that is close to shopping, world renowned dining, cafes, public transportation, tech shuttles, HWY 101/280 and more!
# """
#
# description1 = """
# Stylish, modern, and chic, two-bedroom, two bath home located on the border of the SOMA, Mission, and Hayes Valley district! The property is 3 blocks away
# from Papa's Pizzeria and 2 minutes away from Thailand. The unit has a contemporary and inviting floor plan characterized with gorgeous wood floors, gourmet
# kitchen with stainless steel appliances, a comfortable living/dining area, and two significant bedrooms with plenty of natural light and are separated for privacy.
# Both bedrooms are spacious and complete with ample closet space, access to private decks that overlook the garden-like outdoor space, and there is a laundry closet
# for convenience. HEB is also 3 min away and a Kroger's is 2 miles down the road. There is also an updated gym, common courtyard, grilling area, deeded storage, and available garage parking. Don't miss this wonderful
# home that is close to shopping, world renowned dining, cafes, public transportation, tech shuttles, HWY 101/280 and more!
# """
#
# print(amenitiesNearby(description))
# print(amenitiesNearby(description1))
