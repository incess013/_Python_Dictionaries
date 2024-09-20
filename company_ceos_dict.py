#1
company_ceos_dict = {
"Apple Inc." : "Tim Cook",
"Microsoft Corporation" : "Satya Nadella",
"Amazon.com, Inc." : "Andy Jassy",
"Alphabet Inc." : "Sundar Pichai",
"Tesla, Inc." : "Elon Musk",
"Meta Platforms, Inc." : "Mark Zuckerberg",
"Berkshire Hathaway Inc." : "Warren Buffett",
"Coca-Cola" : "James Quincey",
"Johnson & Johnson" : "Joaquin Duato",
"Netflix, Inc." : "Ted Sarandos",
}

#2
print(company_ceos_dict)

#3
print("The CEO of the 6th company is: ",company_ceos_dict["Meta Platforms, Inc."])

#4
company_ceos_dict["Amazon.com, Inc."] = "Taylor"

#5
del company_ceos_dict['Coca-Cola']

#6
last_key = list(company_ceos_dict.keys())[-1]
last_value = company_ceos_dict[last_key]
print("The last key-value pair is: ", last_key, ":" ,last_value)