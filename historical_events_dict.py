#1
historical_events_dict ={
  "Fall of the Berlin Wall" : 1989,
  "World War I Begins" : 1914,
  "September 11 Attacks" : 2001,
  "American Declaration of Independence" : 1776,
  "World War II Begins" : 1939,
  "Moon Landing" : 1969,
  "COVID-19 Pandemic Declared" : 2020,
  "French Revolution" : 1789,
}   
#2
print(historical_events_dict)

#3
print("The year of the 2nd event is: ",historical_events_dict["World War I Begins"])
      
#4
historical_events_dict["COVID-19 Pandemic Declared"] = "2005"

#5
del historical_events_dict["World War II Begins"]

#6
last_key = list(historical_events_dict.keys())[-1]
last_value = historical_events_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)