#1
university_courses_dict = {
    "Yale": "Drama, History,",
	"Harvard University": "Law, Economics",
	"Stanford University": "Psychology",
	"UC Berkeley": "Environmental Science",
	"Columbia": " Business",
	"University of Chicago" : "Economics Law",
	"Oxford": "Philosophy, Literature",
	"Cambridge": "Mathematics, Engineering",
}

#2
print(university_courses_dict)

#3
print("The course of the 3rd university is: ", university_courses_dict["Stanford University"])

#4
university_courses_dict["Columbia"] = "Music"

#5
del university_courses_dict["Oxford"]

#6
last_key = list(university_courses_dict.keys())[-1]
last_value = university_courses_dict[last_key]
print("The last value-key pair is ", last_key, ":", last_value)	