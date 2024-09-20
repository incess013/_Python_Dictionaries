#1
movie_genres_dict = {
"Action" : "Mad Max",
"Drama" : "The Shawshank Redemption",
"Comedy" : "Superbad",
"Horror" : "Get Out",
"Science Fiction" : "Inception",
"Romance" : "The Notebook",
"Fantasy" :  "The Lord of the Rings",
"Thriller" : "Gone Girl"
}

#2
print(movie_genres_dict)

#3
print("An example movie for the 3rd genre is: ",movie_genres_dict["Comedy"])
      
#4
movie_genres_dict["Science Fiction"] = 'Blade Runner'

#5
del movie_genres_dict["Fantasy"]

#6
last_key = list(movie_genres_dict.keys())[-1]
last_value = movie_genres_dict[last_key]
print("The last key-value pair is: ", last_key, ":",last_value)