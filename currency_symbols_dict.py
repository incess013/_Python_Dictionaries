#1
currency_symbols_dict = {
"Australian Dollar" : "A$",
"British Pound Sterling" : "£",
"Indian Rupee" : "₹",
"Euro " : "€",
"South African Rand" : "R",
"Japanese Yen" : "¥",
"Swiss Franc" : "CHF",
"Canadian Dollar" : "C$",
"Chinese Yuan Renminbi" : "¥" ,
"US Dollar" : "$",
}
#2
print(currency_symbols_dict)

#3
print("The symbol of the 5th currency is: ",currency_symbols_dict["South African Rand"])
      
#4
currency_symbols_dict["Chinese Yuan Renminbi"] = '@'

#5
del currency_symbols_dict["Indian Rupee"]

#6
last_key = list(currency_symbols_dict.keys())[-1]
last_value = currency_symbols_dict[last_key]
print("The last key-value pair is ", last_key ,":",last_value)