#1
video_game_platforms_dict = {
"The Legend of Zelda" : "Nintendo Switch",
"The Last of Us" : "PlayStation 4",
"Minecraft" : "Multi-platform (PC, consoles, mobile)",
"Forza Horizon 5" : "Xbox Series X/S, PC",
"Animal Crossing" : "Nintendo Switch",
"Call of Duty" : "Multi-platform (PC, consoles)",
"Stardew Valley" : "Multi-platform (PC & mobile)",
"Apex Legends" : "Multi-platform (PC, consoles)"
}

#2
print(video_game_platforms_dict)

#3
print("The platform of the 2nd Video game is: ",  video_game_platforms_dict["The Last of Us"])
      
#4
video_game_platforms_dict["Call of Duty"] = 'Playstation'

#5
del video_game_platforms_dict["Forza Horizon 5"]
 
#6
last_key = list(video_game_platforms_dict.keys())[-1]
last_value = video_game_platforms_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)