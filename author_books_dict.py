#1
author_books_dict = {
"Harper Lee" : "To Kill a Mockingbird",
"George Orwell" : "1984",
"Jane Austen" : "Pride and Prejudice",
"F. Scott Fitzgerald" : "The Great Gatsby",
"J.R.R. Tolkien" : "The Hobbit",
"J.K. Rowling" : "Harry Potter and the Sorcerer's Stone",
"Mark Twain" : "The Adventures of Tom Sawyer",
"Gabriel García Márquez" : "One Hundred Years of Solitude"
}
#2
print(author_books_dict)

#3
print("The 5th author's book is: ", author_books_dict["J.R.R. Tolkien"])
      
#4
author_books_dict["Mark Twain"] = "TSWIFT"

#5
del author_books_dict["J.K. Rowling"]

#6
last_key = list(author_books_dict.keys())[-1]
last_value = author_books_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)