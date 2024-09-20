#1
city_landmarks_dict = {
  "Sydney" : "Sydney Opera House",
  "Dubai" : "Burj Khalifa",
  "London" : "Big Ben",
  "Tokyo" : "Tokyo Tower",
  "Paris" : "Eiffel Tower",
  "New York" : "Statue of Liberty",
  "Cairo" : "Pyramids of Giza",
  "Rome" : "Colosseum"
}
#2
print(city_landmarks_dict)

#3
print("The landmark of the 6th city is: ", city_landmarks_dict["New York"])
      
#4
city_landmarks_dict["Dubai"] = "TS"

#5
del city_landmarks_dict["Cairo"]

#6
last_key = list(city_landmarks_dict.keys())[-1]
last_value = city_landmarks_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)