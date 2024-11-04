#strings are array like structures
#arrays are use to store data
#example
marks=[90,60,70]#eg of a list in python
#In arrays the first index must be zero
name= 'cathy'
print(name[0])
print(name[4])

2#looping through strings
#we loop thru strings using a keyword "for"
#forexample
for character in name:
    print(character)


address="kamokya"
for item in address:
    print(item)

#3 slicing in strings
#refer to accessing a range of characters in a string
#example
name="cathy"
print(name[1:3])#at
print(name[1:4])#ath
print(name[1:5])#athy
print(name[0:2])#ca
name="cathy"
print(name[ :4])
message='hello'
print(message[0:3])
#Negative index slice
#always starts from the right side
#example
message="hello"
print(message[-1])#o
print(message[-5])#h
print(message[-1:-5])#blank space
print(message[-1:-4])#blank space
print(message[-5:-3])#he
print(message[-4: ])
print(message[4])
message="hellono"
print(message[ :4])
print(message[4])

# #4. "f"strings
# # these are formatted strings
# #for f strings we embedde variables in curly brackets
# #example
name="Jimia"
age=20
height=56.65
print(f"my name is {name} and I am {age} years old and my height is {height:2f} feet")
total_cost=300000
print(f"A litre of fuel is at {total_cost:,} uganda shillings")
#length #len()

name="Jimia"
print(len(name))
name="JIMIA"
print(len(name))
address="from kamokya"
print(len(address))
name='Jimia\nAli\n'
print(name)