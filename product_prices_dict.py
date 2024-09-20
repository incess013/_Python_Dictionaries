#1
product_prices_dict = {
"Apple iPhone 14" : "$999",
"Samsung Galaxy S23" : "$799",
"Sony WH-1000XM4 Headphones" : "$348",
"Dell XPS 13 Laptop" : "$1,199",
"Fitbit Charge 5" : "$179.95",
"Nintendo Switch" : "$299",
"GoPro HERO10 Black" : "$399",
"Instant Pot Duo 7-in-1" : "$89.99",
"Amazon Echo Dot (4th Gen)" : "$49.99",
"Sony PlayStation 5" : "$499"
}
#2
print(product_prices_dict)

#3
print("The price of the 4th product is: ", product_prices_dict["Dell XPS 13 Laptop"])
   
#4
product_prices_dict["Amazon Echo Dot (4th Gen)"] = '$780.00'

#5
del product_prices_dict["Nintendo Switch"]

#6
last_key = list(product_prices_dict.keys())[-1]
last_value = product_prices_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)