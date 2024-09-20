#1
car_brands_dict = {
	"Toyota" : "Japan",
	"Tesla" : "United States",
	"Hyundai" : "South Korea",
	"Nissan" : "Japan",
	"Honda" : "Japan",
	"BMW" : "Germany",
	"Ford" : "United States",
	"Subaru" : "japan",
	"Audi" : "Germany",
	"BMW" : "Germany",
	"Mercedes-Benz" : "Germany"
	}

#2
print(car_brands_dict)

#3
print("3rd car brand is: ", car_brands_dict['Hyundai'])

#4
car_brands_dict["Ford"] = 'Africa'

#5
del car_brands_dict['Subaru']

#6
last_key = list(car_brands_dict.keys())[-1]
last_value = car_brands_dict[last_key]
print("The last key-value is : " ,last_key, ":", last_value)