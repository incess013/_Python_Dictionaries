#1
holiday_dates_dict = {
"New Year's Day" : "January 1",
"Valentine Day" : "February 14",
"Easter Sunday" : "March",
"Independence Day" : "June 12",
"Halloween" : "October 31",
"Thanksgiving (USA)" : "November",
"Christmas" : "December 25",
"New Year's Eve" : "December 31",
"International Women's Day" : "March 8",
"Labor Day (USA)" : "September"
}
#2
print(holiday_dates_dict)

#3
print("The date of the 4th holiday is: ",holiday_dates_dict["Independence Day"])

#4
holiday_dates_dict["International Women's Day"] = 'September 2'

#5
del holiday_dates_dict['Valentine Day']

#6
last_key = list(holiday_dates_dict.keys())[-1]
last_value = holiday_dates_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)