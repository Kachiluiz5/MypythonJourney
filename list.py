name = ['kachi', 'chidi', 'stella']
print(name)

print(name[0])
print(name[0:2]) #they dont modify our list they only give out a new list
print(name[1:])
name[1] = 'chike'
print(name)

# exersice : write a program to find the largest number in a list
numbers = [2, 5, 3, 6, 10]
max = 3
for number in numbers:
    if number > max:
        max = number
print(f"{max} is the largest number")