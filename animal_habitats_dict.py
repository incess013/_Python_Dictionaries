#1
animal_habitats_dict = {
"Elephant" : "Savannas",
"Polar Bear" : "Arctic sea ice",
"Tiger" : "Forests",
"Clownfish" : "Coral reefs",
"Fox" : "Forests",
"Penguin" : "Antarctic",
"Iguana" : "Rainforests",
"Giant Panda" : "Bamboo forests"
}

#2 
print(animal_habitats_dict)

#3 
print("The habitat of the 3rd animal is: ", animal_habitats_dict["Tiger"])

#4
animal_habitats_dict["Fox"] = 'Tropical forests'

#5
del animal_habitats_dict["Iguana"]

#6
last_key = list(animal_habitats_dict.keys())[-1]
last_value = animal_habitats_dict[last_key]
print("The last key-value pair is " ,last_key, ":", last_value)