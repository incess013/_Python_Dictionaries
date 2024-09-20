#1
dog_breeds_dict = {
"Pug" : "Small",
"Cocker Spaniel" : "Medium",
"Australian Shepherd" : "Medium",
"Rottweiler" : "Large",
"Schnauzer" : "Medium",
"Yorkshire Terrier" : "Small",
"Saint Bernard" : "Large",
"Border Collie" : "Medium",
"French Bulldog" : "Medium",
"Great Dane" : "Large"
}

#2
print(dog_breeds_dict)

#3
print("The size of the 5th breed is: ",dog_breeds_dict ["Schnauzer"])

#4
dog_breeds_dict["Border Collie"] = "Small"

#5
del dog_breeds_dict["Yorkshire Terrier"]

#6
last_key = list(dog_breeds_dict.keys())[-1]
last_value = dog_breeds_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)