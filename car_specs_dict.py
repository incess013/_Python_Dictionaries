#1
car_specs_dict = {
"Toyota Camry" : "203-301 hp",
"Honda Accord" : "192-252 hp",
"Ford F-150" : "290-450 hp",
"Chevrolet Silverado 1500" : "285-420 hp",
"BMW 3 Series" : "154-382 hp",
"Mercedes-Benz C-Class" : "255-385 hp",
"Nissan Altima" : "188-248 hp",
"Volkswagen Golf" : "147-241 hp",
"Hyundai Sonata" : "191-280 hp",
"Subaru Outback" : "182-260 hp"
}
  
#2
print(car_specs_dict)

#3
print("The Horsepower of the 4th car model is: ",car_specs_dict["Chevrolet Silverado 1500"])
      
#4
car_specs_dict["Hyundai Sonata"] = "Horsepower: 999"

#5
del car_specs_dict["BMW 3 Series"]

#6
last_key = list(car_specs_dict.keys())[-1]
last_value = car_specs_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)