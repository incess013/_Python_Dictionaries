#1
app_store_ratings_dict = {
"WhatsApp" : "4.7",
"Instagram" : "4.8",
"Spotify" : "4.5",
"TikTok" : "4.7",
"Zoom" : "4.6",
"Google Maps" : "4.8",
"Slack" : "4.4",
"Duolingo" : "4.7",
"Netflix" : "4.6",
"YouTube" : "4.6"
}

#2
print(app_store_ratings_dict)

#3
print("The rating of the 6th app is: ",app_store_ratings_dict["Google Maps"])

#4
app_store_ratings_dict['Duolingo'] = '5.00'

#5
del app_store_ratings_dict["Netflix"]

#6
last_key = list(app_store_ratings_dict.keys())[-1]
last_value = app_store_ratings_dict[last_key]
print("The last key-value pair is: ", last_key, ":",last_value)