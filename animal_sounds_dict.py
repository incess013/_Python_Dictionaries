#1
animal_sounds_dict = {"Lion": "Roar", 
"Dog": "Woof", "Bird": "Chirps", "Cat": "Meow",
"Frog": "Croak", "Dolphin": "Clicks", "Bee": "Buzz", "Elephant": "Trumpets"
}

#2
print(animal_sounds_dict)

#3
print(animal_sounds_dict["Cat"])

#4
animal_sounds_dict["Bee"] = 'Bizzes'

#5
del animal_sounds_dict["Frog"]

#6
last_key = list(animal_sounds_dict.keys())[-1]
last_value = animal_sounds_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)