#1
phone_models_dict = {
"iPhone 13 Pro" : "Apple",
"Galaxy Z Fold 4" : "Samsung",
"Pixel 6a" : "Google",
"OnePlus Nord 2" : "OnePlus",
"Xperia 5 IV" : "Sony",
"Moto G Power" : "Motorola",
"Nokia X20" : "Nokia",
"Huawei Mate 40 Pro" : "Huawei",
"Oppo Reno 8" : "Oppo",
"Xiaomi Mi 11" : "Xiaomi"

}
#2
print(phone_models_dict)

#3
print("The manufacturer of the 2nd phone model is: ",phone_models_dict["Galaxy Z Fold 4"])

#4
phone_models_dict["Huawei Mate 40 Pro"] = "AB"

#5
del phone_models_dict["Moto G Power"]

#6
last_key = list(phone_models_dict.keys())[-1]
last_value = phone_models_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)