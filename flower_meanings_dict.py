#1
flower_meanings_dict = {
"Rose" : "Love",
"Lily" : "Purity",
"Sunflower" : "Adoration",
"Daisy" : "Innocence",
"Tulip" : "Perfect love",
"Orchid" : "Beauty",
"Chrysanthemum" : "Friendship",
"Lavender" : "Calmness"
} 
#2
print(flower_meanings_dict)

#3
print("The meaning of the 5th flower is: ",flower_meanings_dict["Tulip"])

#4 
flower_meanings_dict["Chrysanthemum"] = 'Soft'

#5
del flower_meanings_dict["Orchid"]

#7
last_key = list(flower_meanings_dict.keys())[-1]
last_value = flower_meanings_dict[last_key]
print("The last key-value pair is " , last_key, ":", last_value)