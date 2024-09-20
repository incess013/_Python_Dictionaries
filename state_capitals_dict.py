#1
state_capitals_dict = {
"California" : "Sacramento",
"Arkansas" : "Little Rock",
"Colorado" : "Denver",
"Alabama" : "Montgomery",
"Alaska" : "Juneau",
"Florida" : "Tallahassee",
"Georgia" : "Atlanta",
"Arizona" : "Phoenix",
"Connecticut" : "Hartford",
"Delaware" : "Dover",
} 
#2
print(state_capitals_dict)

#3
print("The capital of the 4th state is: ",state_capitals_dict["Alabama"])
      
#4
state_capitals_dict["Connecticut"] = "Isabela"

#5
del state_capitals_dict["Georgia"]

#6
last_key = list(state_capitals_dict.keys())[-1]
last_value = state_capitals_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)