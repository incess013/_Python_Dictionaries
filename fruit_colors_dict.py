#1
fruit_colors_dict = {
    "Strawberry" : "Red",
	"Apple" : "Red",
    "Watermelon" : "Green",
	"Blueberry" : "Blue",
	"Grapes" : "Green",
	"Lemon" : "Yellow",
	"Banana" : "Yellow",
	"Orange" : "Orange",
}

#2
print(fruit_colors_dict)

#3
print("The color of the 6th fruit is: ", 'Yellow')

#4
fruit_colors_dict["Blueberry"] = 'Black'

#5
del fruit_colors_dict['Blueberry']

#6
last_key = list(fruit_colors_dict.keys())[-1]
last_value = fruit_colors_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)
