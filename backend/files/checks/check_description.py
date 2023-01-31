import language_tool_python
import check_amenities

# Things to do 
# move readability check here / make sure it works

class descriptionEvaluator:
    def __init__(self,description):
        self.description = description
        self.grammar_tool = language_tool_python.LanguageTool('en-US')

    def add_description(self,description):
        self.description = description

    def clear_description(self):
        self.description = ''

    def grammar_check(self):
        matches = self.grammar_tool.check(self.description)
        # processed_matches = self.grammar_spelling_match_parser(matches)
        return matches

    def grammar_spelling_match_parser(matches):
        # write out logic to filter out matches we don't care about
        return matches

    def nearby_attractions_check(self):
        # if result[0] is True, user was specific mentioned amenities
        # if result[1] is True, that means user informed guests of distances to amenities well
        return check_amenities.find_nearby_amenities(self.description)
    
def test_description_evaluator():
    description = """
About this space
Enjoy a luxe all-suite layout, a sleek full kitchen, and stunning Gulf views on your private covered balcony! As part of the Origin Beach Resort, this modern 1BR retreat that sleeps 6 features outdoor pool and hot tub, fitness center, game room and a very large common area observation deck with breathtaking gulf views.
The space
ABSOLUTELY STUNNING*This BEAUTIFULLY RENOVATED / 1 bed 1 bath condo has been completely renovated to meet the upscale taste of the owner. Renovations include: Refurbished kitchen cabinets with new hardware, completely renovated bathroom with a walk-in tiled shower and double sink vanity, wood look tile throughout the main living area and master bedroom, freshly painted, upgraded furniture, new hot water heater in 2021 and is an ABSOLUTE MUST SEE!!. Origin at Seahaven has unsurpassed amenities which include a gulf view pool & hot tub, sunrise and sunset observation decks, grilling & gathering decks, fitness room, movie theater and game room. Origins FANTASTIC beach location is steps to Pier Park, shopping and dining
Other things to note
Please be aware that there will be NO refunds for Wifi issues as it’s not guaranteed at the beach. If reliable wifi is a must you are welcome to bring your own internet hotspot.
    """
    evaluator = descriptionEvaluator(description)
    print(evaluator.grammar_check())
    print(evaluator.nearby_attractions_check())


test_description_evaluator()