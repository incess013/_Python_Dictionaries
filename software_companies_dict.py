#1
software_companies_dict = {
    "Adobe": "San Jose, California, USA",
	"Google (Alphabet Inc.)": "Mountain View", 
	"Intuit": "Mountain View, California, USA",
	"VMware": "Palo Alto, California, USA",
	"Microsoft": "Redmond, Washington, USA",
	"Oracle": "Austin, Texas, USA",
	"Apple": "Cupertino, California, USA",
	"SAP": "Walldorf, Germany",
	"IBM": "Armonk, New York, USA",
	"Salesforce": "San Francisco, California, USA"
}

#2
print(software_companies_dict)

#3
print("The headquarters of the 3rd company is: ", 'Mountain View, California, USA')

#4
software_companies_dict["SAP"] = 'Isabela'

#5
del software_companies_dict['IBM']

#6
last_key = list(software_companies_dict.keys())[-1]
last_value = software_companies_dict[last_key]
print("The last key-value is ",last_key, ":", last_value)