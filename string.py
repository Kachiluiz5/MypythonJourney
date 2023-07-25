word1 = "its john's pen " #correct
word2 = 'the "EXAMINATION" will commence'
print(word1)
print(word2)

# multiple line strings

multi_string = """ hi jaoh is is the firrst
email we seek your response."""

print(multi_string)
print(multi_string[1])
print(multi_string[-2])
print(multi_string[0:4]) # will get characters starting from 0 - 4 but wont get the 4th craacter
print(multi_string[0:]) #it will get all the character

# class work
the_name = "jenifer"
print(the_name[0:-1])


# formatted strings
# joh [smith] is a coder
first = 'john'
last = 'smith'
msg = first + ' [' + last + '] is a coder'
print(msg)
message = f"{first} [{last}] is a coder"
print(message)





