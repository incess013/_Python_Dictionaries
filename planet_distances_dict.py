#1
planet_distances_dict = {
"Mercury" : "57.91 million km",
"Venus" : "108.21 million km",
"Earth" : "149.60 million km",
"Mars" : "227.94 million km",
"Jupiter" : "778.57 million km",
"Saturn" : "1,429.99 million km",
"Uranus" : "2,870.97 million km",
"Neptune" : "4,498.25 million km"
}

#2
print(planet_distances_dict)

#3
print("The distance of the 3rd planet is: ",planet_distances_dict["Earth"])
      
#4
planet_distances_dict["Jupiter"] = '999.99 million km'

#5
del planet_distances_dict["Uranus"]

#6
last_key = list(planet_distances_dict.keys())[-1]
last_value = planet_distances_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)