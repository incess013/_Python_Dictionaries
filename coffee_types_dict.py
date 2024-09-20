#1
coffee_types_dict = {
"Espresso" : "Strong, concentrated coffee brewed with hot water.",
"Americano" : "Espresso diluted with hot water.",
"Latte" : "Espresso with steamed milk and a bit of foam.",
"Cappuccino" : "Equal parts espresso, steamed milk, and foam.",
"Macchiato" : "Espresso stained with a bit of milk.",
"Mocha" : "Espresso with steamed milk and chocolate syrup.",
"Flat White" : "Strong coffee with velvety microfoam.",
"Cold Brew" : "Coffee brewed cold for a smooth taste.",
"Affogato" : "Espresso poured over vanilla ice cream.",
"Turkish Coffee" : "Finely ground coffee brewed unfiltered."
}
#2
print(coffee_types_dict)

#3
print("The 4th type of coffee description: ",coffee_types_dict["Cappuccino"])
      
#4
coffee_types_dict["Cold Brew"] = "FAVE"

#5
del coffee_types_dict["Macchiato"]

#6
last_key = list(coffee_types_dict.keys())[-1]
last_value = coffee_types_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)