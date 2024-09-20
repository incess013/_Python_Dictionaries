#1
artist_songs_dict = {
"Taylor Swift" : "Shake It Off",
"Ed Sheeran" : "Shape of You",
"Beyoncé" : "Crazy In Love",
"Drake" : "God's Plan",
"Adele" : "Rolling in the Deep",
"The Weeknd" : "Blinding Lights",
"Billie Eilish" : "Bad Guy",
"Bruno Mars" : "Uptown Funk"
}
  
#2
print(artist_songs_dict)

#3
print("The top song of the 3rd artist is: ",artist_songs_dict["Beyoncé"])
      
#4
artist_songs_dict["The Weeknd"] = "Die for You"

#5
del artist_songs_dict["Billie Eilish"]

#6
last_key = list(artist_songs_dict.keys())[-1]
last_value = artist_songs_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)