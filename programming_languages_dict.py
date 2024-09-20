#1
programming_language_dict = {
"C" : "Dennis Ritchie",
"C++" : "Bjarne Stroustrup",
"Java" : "James Gosling",
"Python" : "Guido van Rossum", 
"Ruby" : "Yukihiro Matsumoto",
"JavaScript" : "Brendan Eich",
"PHP" : "Rasmus Lerdorf"
}

#2 
print(programming_language_dict)

#3
print("The 4th programming language and the developers is: ", programming_language_dict['Python'])

#4
programming_language_dict["JavaScript"] = "A"

#5
del programming_language_dict["C++"]

#6
last_key = list(programming_language_dict.keys())[-1]
last_value = programming_language_dict[last_key]
print("The last key-value is: ", last_key, ":", last_value)