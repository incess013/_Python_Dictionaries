 #1
country_capital_dict = {
"Norway": "Oslo",
"Greece": "Athens",
"Finland": "Helsinki",
"Latvia": "Riga",
"Denmark": "Copenhagen",
"Ireland": "Dublin",
"North Macedonia": "Skopje",
"Lithuania": "Vilnius",
"Portugal": "Lisbon",
"Estonia": "Tallinn",
"Slovakia": "Bratislava",
"Albania": "Tirana"
}

#2
print(country_capital_dict)

#3
print("The capital of the 5th country is: ",country_capital_dict['Denmark'])

#4
country_capital_dict["Lithuania"] = "Manila"

#5
del country_capital_dict["Slovakia"]

#6
last_key = list(country_capital_dict.keys())[-1]
last_value = country_capital_dict[last_key]
print("The last key-value is: ", last_key, ":",last_value)