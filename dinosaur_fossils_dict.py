#1
dinosaur_fossils_dict = {
    "Velociraptor" : "Mongolia",
    "Stegosaurus" : "North America",
    "Brachiosaurus" : "North America, Africa",
    "Spinosaurus" : "North Africa",
    "Ankylosaurus" : "North America",
    "Tyrannosaurus Rex" : "North America",
    "Triceratops" : "North America"
} 
#2
print(dinosaur_fossils_dict)

#3
print("Location of the 4th dinousaur's fossils:  ",dinosaur_fossils_dict["Spinosaurus"])
      
#4
dinosaur_fossils_dict["Stegosaurus"] = "USA"

#5
del dinosaur_fossils_dict["Tyrannosaurus Rex"]

#6
last_key = list(dinosaur_fossils_dict.keys())[-1]
last_value = dinosaur_fossils_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)