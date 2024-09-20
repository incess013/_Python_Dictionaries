#1
food_recipes_dict = {
"Spaghetti Aglio e Olio" : "Cook spaghetti, sauté garlic in olive oil, mix with pasta, and garnish with parsley.",

"Chicken Stir-Fry" : "Sauté chicken, add bell peppers and broccoli, stir in soy sauce, and cook until tender.",

"Caprese Salad" : "Layer mozzarella and tomatoes, sprinkle with basil, drizzle with olive oil and balsamic vinegar.",

"Tacos" : "Cook ground beef, fill tortillas, and top with lettuce, cheese, and salsa.",

"Omelette" : "Whisk eggs, pour into a pan, add cheese and veggies, cook until set, and fold.",

"Chocolate Chip Cookies" : "Cream butter and sugar, mix in eggs, add flour and chocolate chips, scoop, and bake.",

"Vegetable Soup" : "Sauté mixed veggies, add vegetable broth, herbs, and simmer.",

"Pancakes" : "Mix flour, milk, eggs, and baking powder; pour on skillet, cook until bubbles form."
}
#2
print(food_recipes_dict)

#3
print("The 5th food recipes are: ", food_recipes_dict["Omelette"])
      
#4
food_recipes_dict["Caprese Salad"] = "Cheese"

#5
del food_recipes_dict["Vegetable Soup"]

#6
last_key = list(food_recipes_dict.keys())[-1]
last_value = food_recipes_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)