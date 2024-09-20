#1
city_population_dict = {
"Quezon City": "2,761,720",
"Manila": "1,600,000",
"Caloocan City": "1,500,000",
"Budta": "1,273,715",
"Davao": "1,212,504", 
"Malingao":	"1,121,974",
"Cebu City": "798,634",
"General Santos": "679,588",
"Taguig": "644,473",
"Pasig City": "617,301"
}

#2
print(city_population_dict)

#3
print("The population of the 6th city is: ", city_population_dict['Malingao'])

#4
city_population_dict['Caloocan City'] = '1,800,000'

#5
del city_population_dict["Taguig"]

#6
last_key = list(city_population_dict.keys())[-1]
last_value = city_population_dict[last_key]
print("The last key-value is ", last_key, ":", last_value)