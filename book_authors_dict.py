#1
book_authors_dict = {
    "Brave New World" : "Aldous Huxley",
	"The Picture of Dorian Gray" : "Oscar Wilde",
	"To kill a mockingbird" : "Harper Lee",
	"The catcher in the Rye" : "J.D. Salinger",
	"The Adventures of Huckleberry Finn" : "Mark Twain",
	"Fahrenheit 451" : "Ray Bradbury",
	"The Odyssey" : "Homer",
	"Frankenstein" : "Mary Shelley",
	"Pride and Prejudice" : "Jane Austen",
	"1984" : "George Orwell",
	"The Great Gatsby" : "F. Scott Fitzgerald",
	"Moby-Dick" : "Herman Melville",
}

#2
print(book_authors_dict)

#3
print("The 9th book is ",book_authors_dict['Pride and Prejudice'])

#4
book_authors_dict["The Adventures of Huckleberry Finn"] = 'Taylor'

#5
del book_authors_dict['To kill a mockingbird']

#6
last_key = list(book_authors_dict.keys())[-1]
last_value = book_authors_dict[last_key]
print("The last key-value is ", last_key, ":" ,last_value)