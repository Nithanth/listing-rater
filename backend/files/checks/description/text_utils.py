import nltk.tokenize

def tokenize_description(description):
    tokens = nltk.tokenize.word_tokenize(description)
    count = 0
    while count != len(tokens):
        token = tokens[count]
        if (token == ',' or token == '' or token == '!' or token == '.'):
            tokens.pop(count)
        else:
            count += 1
    return tokens

description = """
Stylish, modern, and chic, two-bedroom, two bath home located on the border of the SOMA, Mission, and Hayes Valley district!
The unit has a contemporary and inviting floor plan characterized with gorgeous wood floors, gourmet kitchen with stainless steel appliances,
a comfortable living/dining area, and two significant bedrooms with plenty of natural light and are separated for privacy. Both bedrooms are
spacious and complete with ample closet space, access to private decks that overlook the garden-like outdoor space, and there is a laundry closet
for convenience. There is also an updated gym, common courtyard, grilling area, deeded storage, and available garage parking. Don't miss this wonderful
home that is close to shopping, world renowned dining, cafes, public transportation, tech shuttles, HWY 101/280 and more!
"""
