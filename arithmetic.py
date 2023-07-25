print(10) #integer
print(10.33) #float

print(10 + 3) #addition
print(10 - 3) #subtraction
print(10 * 3) #multiplication
print(10 / 3) #division but will return it in float
print(10 // 3) #divition but will return it as an integer
print(10 % 3) #module this return the reminder of the division
print(10 ** 3) #exponent this will return 10 in the power of 3 10*10*10

# argumented assignment
# before
x = 10
x = x + 3
print(x)

# after(using argumented assignment operator)
x = 10
x += 3  #applicable to other operators (x -= 3)
print(x)


# operator presedence (just like the BODMAS)
# but in programming its:
# 1. exponentation (2 ** 3)
# 2. multiplication or division ( * or / or //)
# 3. addition or subtraction (+ or -)
x = 10 + 3 * 2 ** 2
# if parenteses is added it comes first
x = (10 + 3) * 2 ** 2
print(x)

