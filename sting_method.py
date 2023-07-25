info = "Hello Python Developer"
print(len(info))  #print and len() are general purpose function and not a method

# python method
print(info.upper())
print(info.lower())
# methods do not change or modify our string rater it create a new string and returns it
print(info.find('P')) #the will find the character and return the index number
print(info.find('Developer'))

# replacing characters using the replace method()
print(info.replace('Developer', 'Engineer'))

# checking if a character is present in a string of characters using the (in operator)
print('D' in info) #this is called an expression (boolean expresion)