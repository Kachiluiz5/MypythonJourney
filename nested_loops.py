# adj = range(3)
# fruits = range(4)
#
# for x in adj:
#     for y in fruits:
#         print(x, y)
# for a in adj:   # passed statement
#     pass


# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

# EXERSICE

# number = [5, 2, 5, 2, 2]
# a = 'x'                         #BAD METHOD
# for num in number:
#     for i in a:
#         print(f"{num * i}")


numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    result = ''
    for count in range(x_count):
        result += 'x'
    print(result)
