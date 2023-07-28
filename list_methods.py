# numbers = [5, 2, 11, 7, 4]

# numbers.append(10)


# numbers.insert(0, 31)
# numbers.remove(2)
# numbers.clear()
# numbers.pop() #remove the last item on our list
# numbers.index()
# numbers.count()
# print(50 in numbers)  #CHECKING IF AN INDEX IS AVALILABLE IN THE LIST
# print(numbers)

# sorting
# numbers.sort()
# numbers.reverse()
# print(numbers)

# copy
# number2 = numbers.copy()
# print(number2)
# numbers.append(22)
# print(numbers)

# exersize
# write a program to remove the duplicates in a list
list = [1, 3, 4, 3, 5, 7, 5, 8]
uniques = []

for num in list:
    if num not in uniques:
        uniques.append(num)
print(uniques)

