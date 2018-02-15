import cc_data

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_cc_data_file_from_json(json_data):
    cc_data_file = cc_data.CCDataFile()

    for json_level in json_data:
        cc_level = cc_data.CCLevel()
        cc_level.level_number = json_level["level_number"]
        cc_level.num_chips = json_level["num_chips"]
        cc_level.time = json_level["time"]
        cc_level.upper_layer = json_level["upper_layer"]
        cc_level.lower_layer = json_level["lower_layer"]

        #still need to handle optional fields
        json_fields = json_level ["optional_fields"]
        for json_field in json_fields:
            field_type = json_field["type"]
            if (field_type == "title"):
                title = json_field["title"]
                cc_title_field = cc_data.CCMapTitleField(title)
                cc_level.add_field(cc_title_field)
            elif (field_type == "hint"):
                hint = json_field["hint"]
                CCMapHintField = cc_data.CCMapHintField(hint)
                cc_level.add_field(CCMapHintField)
            else:
                print ("I don't know what that was")
        #now I need to do the above for all the rest of the optional fields

        cc_data_file.add_level(cc_level)
    return cc_data_file
