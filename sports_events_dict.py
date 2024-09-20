#1
sports_events_dict = {
"Olympic Games" : "2021 (Tokyo)",
"FIFA World Cup" : "2022 (Qatar)",
"Super Bowl" : "2023",
"Wimbledon" : "2023",
"Tour de France" : "2023",
"NBA Finals" : "2023",
"The Masters ": "2023"
}
#2
print(sports_events_dict)

#3
print("the 3rd sports event year is: ",sports_events_dict["Super Bowl"])
      
#4
sports_events_dict["NBA Finals"] = "2040"

#5
del sports_events_dict ["Tour de France"]

#6
last_key = list(sports_events_dict.keys())[-1]
last_value = sports_events_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)