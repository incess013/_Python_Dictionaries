#1
movie_directors_dict = {
"The Godfather" : "Francis Ford Coppola", 
"Pulp Fiction" :  "Quentin Tarantino",
"Inception" : "Christopher Nolan",
"Schindler's List": "Steven Spielberg",
"The Shawshank Redemption" : "Frank Darabont",
"Fight Club" : "David Fincher",
"The Dark Knight" : "Christopher Nolan",
"Forrest Gump" : "Robert Zemeckis",
"Interstellar" : "Christopher Nolan",
"The Matrix" : "Lana and Lilly Wachowski"
}

#2 
print(movie_directors_dict)

#3
print("The director of the 5th movie is: ",'Frank Darabont')

#4
movie_directors_dict["Interstellar"] = 'Taylor'

#5
del movie_directors_dict["The Dark Knight"]

#6
last_key = list(movie_directors_dict.keys())[-1]
last_value = movie_directors_dict[last_key]
print("The last key-value pair is ", last_key, ":" ,last_value)