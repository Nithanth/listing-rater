import tokenize_description

amenities = [
    "swimming"
    "pool",
    "swimming pool",
    "hot tub",
    "jacuzzi",
    "billiard",
    "billiards",
    "ping pong",
    "table tennis",
    "tree house",
    "wine rack",
    "bar cart",
    "fireplace"
]

# Iterate through description and look for amenities listed which are defined above
class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def add_word(self,word):
        curr = self

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        
        curr.end_of_word = True

    def search_word(self,word):
        cur = self

        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        
        if cur.end_of_word:
            return True

        return False

def build_amenity_tree(amenities):
    word_trie = TrieNode()
    for amenity in amenities:
        word_trie.add_word(amenity)

    return word_trie

def check_amenities(description):
    amenities_found = []
    word_trie = build_amenity_tree(amenities)

    # write function to break up description into array and cut out commas / punctuation -> steal from other file
    tokens = tokenize_description.tokenize_description(description)

    # call search function in word_trie to validate words
    print(tokens)
    for word in tokens:
        if word_trie.search_word(word):
            amenities_found.append(word)
    
    return amenities_found

def test():
    description = """ Stylish, modern, and chic, two-bedroom, two bath home located on the border of the SOMA, Mission, and Hayes Valley distric complete with a swimming pool!
            The unit has a contemporary and inviting floor pool characterized with gorgeous wood floors, gourmet kitchen with stainless steel appliances,
            a comfortable living/dining area, and two significant bedrooms with plenty of natural light and are separated for privacy. Both bedrooms are
            spacious and complete with ample closet space, access to private decks that overlook the garden-like outdoor space, and there is a laundry closet
            for convenience. There is also an updated gym, common courtyard, grilling area, deeded storage, and available garage parking. Don't miss this wonderful
            home that is close to shopping, world renowned dining, cafes, public transportation, tech shuttles, HWY 101/280 and more! A fireplace is in the living room along with a billiard
            """

    print(check_amenities(description))

test()