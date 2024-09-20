#1
plant_types_dict = {
"Rosemary" : "Herb",
"Maple" : "Tree",
"Lavender" : "Herb",
"Holly" : "Shrub",
"Oak" : "Tree",
"Basil" : "Herb",
"Hydrangea" : "Shrub",
"Pine" : "Tree"
} 
#2
print(plant_types_dict)

#3
print("The type of the 5th plant is: ",plant_types_dict ["Oak"])
      
#4
plant_types_dict["Maple"] = "Flower"

#5
del plant_types_dict["Basil"]

#6
last_key = list(plant_types_dict.keys())[-1]
last_value = plant_types_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)