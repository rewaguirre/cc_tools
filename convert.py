import cc_dat_utils

#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
# cc_dat = cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat")
# print(cc_dat)
#print the resulting data
#cc_dat = cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat")
#print(cc_dat)


#Part 2 Example
example_json_file = "data/example_json.json"
#Open the file specified by example_json_file
#Use the json module to load the data from the file
#Use make_family_from_json(json_data) to convert the data to Family data
#Print out the resulting Family data using print()
#End Part 2 Example


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
import json
import test_data
import test_json_utils
#def make_game_library_from_json(json_data):
 #   new_game_library = test_json_utils.game_library()
 #   return new_game_library

with open("data/test_data.json", 'r') as reader:
    json_data = json.load(reader)
game_library = test_json_utils.make_game_library_from_json(json_data)
print (game_library)
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###


#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file