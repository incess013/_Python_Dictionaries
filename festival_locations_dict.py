#1
festival_locations_dict = {
"Carnival" : "Rio de Janeiro, Brazil",
"Diwali" : "India (nationwide)",
"Oktoberfest" : "Munich, Germany",
"Holi" : "India (widely celebrated)",
"La Tomatina" : "Buñol, Spain",
"Mardi Gras" : "New Orleans, USA",
"Gion Matsuri" : "Kyoto, Japan",
"Running of the Bulls" : "Pamplona, Spain"
}
#2
print(festival_locations_dict)

#3
print("The 4th festival is being held at: ",festival_locations_dict["Holi"])
      
#4
festival_locations_dict["Mardi Gras"] = "USA"

#5
del festival_locations_dict["Diwali"]

#6
last_key = list(festival_locations_dict.keys())[-1]
last_value = festival_locations_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)