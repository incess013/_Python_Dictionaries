#1
beaches_countries_dict = {
"Copacabana Beach" : "Brazil",
"Maya Bay" : "Thailand",
"Waikiki Beach" : "USA (Hawaii)",
"Anse Source d'Argent" : "Seychelles",
"Bondi Beach" : "Australia",
"Zlatni Rat" : "Croatia",
"Playa del Carmen" : "Mexico",
"Whitehaven Beach" : "Australia"
}
#2
print(beaches_countries_dict)

#3
print("The 3rd beach is located at: ",beaches_countries_dict["Waikiki Beach"])
      
#4
beaches_countries_dict["Zlatni Rat"] = "PH"

#5
del beaches_countries_dict["Bondi Beach"]

#6
last_key = list(beaches_countries_dict.keys())[-1]
last_value = beaches_countries_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)