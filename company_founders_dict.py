#1
company_founders_dict = {
"Apple Inc." : "Steve Jobs, Steve Wozniak, Ronald Wayne",
"Microsoft Corporation" : "Bill Gates, Paul Allen",
"Amazon.com, Inc." : "Jeff Bezos",
"Google (Alphabet Inc.)" : "Larry Page, Sergey Brin",
"Facebook (Meta Platforms, Inc.)" : "Mark Zuckerberg, Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, Chris Hughes",
"Tesla, Inc." :" Elon Musk, Martin Eberhard, Marc Tarpenning, JB Straubel, Ian Wright",
"Nike, Inc." : "Phil Knight, Bill Bowerman",
"Coca-Cola Company" : "John Stith Pemberton"
}   
    
#2
print(company_founders_dict)

#3
print("The founder of the 6th company is: ",company_founders_dict["Tesla, Inc."])
      
#4
company_founders_dict["Microsoft Corporation"] = "Swift"

#5
del company_founders_dict["Coca-Cola Company"]

#6
last_key = list(company_founders_dict.keys())[-1]
last_value = company_founders_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)