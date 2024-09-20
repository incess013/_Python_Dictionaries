#1
athlete_achievements_dict = {
"Roger Federer" : "Greatest Achievement: Winner of 20 Grand Slam singles titles, including a record eight Wimbledon titles.",
"LeBron James" : "Greatest Achievement: Four-time NBA champion and four-time NBA MVP, with multiple All-Star selections.",
"Jackie Joyner-Kersee" : "Greatest Achievement: Two-time Olympic heptathlon gold medalist and holds the world record in the heptathlon.",
"Cristiano Ronaldo" : "Greatest Achievement: Winner of 5 Ballon d'Or awards and holds the record for most goals in UEFA Champions League history.",
"Katie Ledeck" : "Greatest Achievement : Winner of 7 Olympic gold medals in swimming, with multiple world records in distance events.",
"Pele" : "Greatest Achievement: Three-time FIFA World Cup champion and regarded as one of the greatest footballers of all time.",
"Diana Taurasi" : "Greatest Achievement : WNBA champion and multiple-time MVP, with numerous scoring titles and Olympic gold medals.",
"Michael Jordan": "Greatest Achievement: Six-time NBA champion and five-time NBA MVP, known for his impact on the game of basketball."
}
#2
print(athlete_achievements_dict)

#3
print("The achievement of the 5th athlete is: ",athlete_achievements_dict["Katie Ledeck"])
      
#4
athlete_achievements_dict["Jackie Joyner-Kersee"] = "Champion 2024"

#5
del athlete_achievements_dict["Diana Taurasi"]

#6
last_key = list(athlete_achievements_dict.keys())[-1]
last_value = athlete_achievements_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)