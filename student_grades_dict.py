#1
student_grades_dict = {
	"Student1" : "80",
	"Student2" : "85",
	"Student3": "90",
	"Student4" : "95",
	"Student5" : "97"
}

#2
print(student_grades_dict)

#3
print("Grade of the third student is ",student_grades_dict['Student3'])

#4
student_grades_dict['Student2'] = 'A'

#5
del student_grades_dict['Student5']

#6
last_key = list(student_grades_dict.keys())[-1]
last_value = student_grades_dict[last_key]
print("The last key-value is ", last_key, ":" ,last_value)