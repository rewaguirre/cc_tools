import sys
import json
import test_data
input_json_file = "data/test_data.json"
with open("data/test_data.json", 'r') as reader:
    json_data = json.load(reader)

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    for game_data in json_data["Games"]:
        game = test_data.Game()
        for platform_data in game_data["Platform"]:
            platform = test_data.Platform()
            platform.name = platform_data["Name"]
            platform.launch_year = platform_data["Launch Year"]
        game.name = game_data["Title"]
        game.year = game_data["Year"]
        game_library.add_game(game)


    #print(json_data[game])
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    #Return the completed game_library

    return game_library
