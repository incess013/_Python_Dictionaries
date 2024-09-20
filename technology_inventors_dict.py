#1
technology_inventors_dict = {
"World Wide Web" : "Tim Berners-Lee",
"Telephone" : "Alexander Graham Bell",
"Light Bulb" : "Thomas Edison",
"Internet" : "Vint Cerf and Bob Kahn",
"Computer" : "Charles Babbage",
"Radio" : "Guglielmo Marconi"
}
#2
print(technology_inventors_dict)

#3
print("The inventor of the 4th technology is: ",technology_inventors_dict["Internet"])
      
#4
technology_inventors_dict["Telephone"] = 'Swift'

#5
del technology_inventors_dict["Radio"]

#6
last_key = list(technology_inventors_dict.keys())[-1]
last_value = technology_inventors_dict[last_key]
print("The last key-value pair is ", last_key, ":",last_value)