import sys
import json
import test_data
input_json_file = "data/test_data.json"
with open("data/test_data.json", 'r') as reader:
    json_data = json.load(reader)

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(test_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    print("hi")
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    #Return the completed game_library

    return game_library
