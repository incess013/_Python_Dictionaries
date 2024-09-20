#1
technology_innovators_dict = {
  "Airplane" : "Wright Brothers",
  "Smartphone" : "Steve Jobs",
  "GPS" : "Roger L. Easton",
  "Personal Computer" : "Steve Jobs and Steve Wozniak",
  "Internet" : "Tim Berners-Lee",
  "Electric Light Bulb" : "Thomas Edison",
  "Telephone" : "Alexander Graham Bell",
  "Automobile" : "Henry Ford"
}
#2
print(technology_innovators_dict)

#3
print("The 4th technology innovator is: ",technology_innovators_dict["Personal Computer"])
      
#4
technology_innovators_dict["Smartphone"] = "ABC"

#5
del technology_innovators_dict ["Electric Light Bulb"]

#6
last_key = list(technology_innovators_dict.keys())[-1]
last_value = technology_innovators_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)