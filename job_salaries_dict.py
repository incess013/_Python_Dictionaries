#1
job_salaries_dict = {
"Graphic Designer" : "$55,000",
"Mechanical Engineer" : "$85,000",
"Web Developer" : "$80,000",
"Project Manager" : "$85,000",
"Teacher" : "$60,000",
"Registered Nurse" : "$75,000",
"Marketing Manager" : "$90,000",
"Software Engineer" : "$110,000",
"Data Scientist" : "$120,000",
 "Accountant" : "$70,000"
}
#2
print(job_salaries_dict)

#3
print("The salary of the 3rd job is: ",job_salaries_dict ["Web Developer"])
      
#4
job_salaries_dict["Marketing Manager"] = "$999,000"

#5
del job_salaries_dict["Data Scientist"]

#6
last_key = list(job_salaries_dict.keys())[-1]
last_value = job_salaries_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)