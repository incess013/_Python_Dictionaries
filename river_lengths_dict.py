#1
river_lengths_dict = {
"Amazon River" : "7,062 km",
"Nile River" : "6,650 km",
"Yangtze River" : "6,300 km",
"Mississippi River" : "3,734 km",
"Yenisei River": "5,539 km",
"Yellow River" : "5,464 km,"
}

#2 
print(river_lengths_dict)

#3
print("The length of the 2nd river is approximately: ",river_lengths_dict["Nile River"])

#4 
river_lengths_dict["Yenisei River"] = "6,000km"

#5
del river_lengths_dict['Yenisei River']

#6
last_key = list(river_lengths_dict.keys())[-1]
last_value = river_lengths_dict[last_key]
print("The last key-value pair is ", last_key, ":", last_value)