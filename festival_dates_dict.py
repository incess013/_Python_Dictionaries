#1
festival_dates_dict = {
"New Year's Day" : "January 1",
"Valentine Day" : "February 14",
"Holi" : "March",
"Eid al-Fitr" : "April",
"Independence Day (USA)" : "July 4",
"Diwali" : "October",
"Halloween" : "October 31",
"Thanksgiving (USA)" : "November 4",
"Christmas" : "December 25",
"New Year's Eve" : "December 31"
}   
    
#2
print(festival_dates_dict)

#3
print("The date of the 3rd festival is: ",festival_dates_dict["Holi"])
      
#4
festival_dates_dict["Halloween"] = "October 6"

#5
del festival_dates_dict["Independence Day (USA)"]

#6
last_key = list(festival_dates_dict.keys())[-1]
last_value = festival_dates_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)