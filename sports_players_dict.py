#1
sports_players_dict = { 
    "Golf": "Tiger Woods",
	"Boxing": "Muhammad Ali",
	"Rugby": "Richie McCaw",
	"Basketball": "Michael Jordan",
	"Tennis": "Serena Williams",
	"Baseball": "Babe Ruth",
	"Hockey": "Wayne Gretzky",
	"American Football": "Tom Brady",
	"Soccer": "Pelé",
	"Cricket": "Sachin Tendulkar"
}

#2 
print(sports_players_dict)

#3
print("The player of the 4th sports is: ",sports_players_dict["Basketball"])

#4
sports_players_dict['Baseball'] = "Taylor"

#5
del sports_players_dict['Cricket']

#6
last_key = list(sports_players_dict.keys())[-1]
last_value = sports_players_dict[last_key]
print("The last key-value pair is: ", last_key , ":", last_value)
