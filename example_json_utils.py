import sys
import json
import example_data

#Creates and returns a Family object(defined in example_data) from loaded json_data
def make_family_from_json(json_data):
    #Initialize a new family
    new_family = example_data.Family()
    #trying to make this myself
    new_family.parent1 = json_data["Parent1"]
    new_family.parent2 = json_data["Parent2"]
    for kid_data in json_data["Kids"]:
        new_kid = example_data.Kid()
        new_kid.name = kid_data["Name"]
        new_kid.age = kid_data["Age"]

        new_family.add_kid(new_kid)

    #Set the parents
    #Loop through the kids_data and make a new Kid for each entry in the kids_data
    #Note: this is how to loop through data in python
    #One thing to note is "kid_data" is a variable that is declared as part of the loop
    #  The loop steps through each element in the list (here the list is kids_data)
    #  and the variable kid_data represents the current element in the list
        #Get the data from from the current kid in the kids_data list
        #Make a new Kid with the data
        #Add the Kid to the new_family
    #We're done making and adding all the kids, so return the finished Family
    return new_family