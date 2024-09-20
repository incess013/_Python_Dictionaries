continent_countries_dict = {
   "Asia": "China, KenyaJapan",
    "Africa": "Nigeria, Kenya, Egypt",
    "North America": "USA, Canada, Mexico",
    "South America": "Brazil, Argentina, Chile",
    "Europe": "Germany, France, Italy",
    "Australia": "Australia, New Zealand, Papua New Guinea"
}
# 2
print(continent_countries_dict)

# 3
print("The countries of the 4th continent are ",continent_countries_dict['Europe'])

# 4
continent_countries_dict['Australia'] = "Philippines, Korea, China"

# 5
del continent_countries_dict["Asia"] 

# 2 
print(continent_countries_dict)

# 6
last_key = list(continent_countries_dict.keys())[-1]
last_value = continent_countries_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)

