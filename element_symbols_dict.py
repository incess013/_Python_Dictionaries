#1
element_symbols_dict = {
"Hydrogen" : "H",
"Helium" : "He",
"Lithium" : "Li",
"Carbon" : "C",
"Nitrogen" : "N",
"Oxygen" : "O",
"Fluorine" : "F",
"Neon" : "Ne",
"Sodium" : "Na",
"Magnesium" : "Mg",
}

#2
print(element_symbols_dict)

#3
print("The symbol of the 6th element is: ",element_symbols_dict['Oxygen'])

#4
element_symbols_dict["Neon"] = 'X'

#5
del element_symbols_dict["Sodium"]

#6
last_key = list(element_symbols_dict.keys())[-1]
last_value = element_symbols_dict[last_key]
print("The last key-value pair is ", last_key, ":" , last_value)
 