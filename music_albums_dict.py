#1
music_albums_dict = {
"Taylor Swift" : "(2006)",
"Speak Now" : "(2010)",
"Reputation" : "(2017)",
"Lover" : "(2019)",
"Folklore" : "(2020)",
"Evermore" : "(2020)",
"Red (Taylor's Version)" : "(2021)",
"Midnights" : "(2022)",
"Speak Now (Taylor's Version)" : "(2023)",
"The Tortured Poets Department" : "(2024)",
}
#2
print(music_albums_dict)

#3
print("The release year of the 3rd album is: ",music_albums_dict["Reputation"])
      
#4
music_albums_dict["Midnights"] = "0013"

#5
del music_albums_dict["Folklore"]

#6
last_key = list(music_albums_dict.keys())[-1]
last_value = music_albums_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)