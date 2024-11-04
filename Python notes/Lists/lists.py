#Lists are mutable, it also works with index
#item stored should be the same
studentNames = ['Shakira','Edith','Cathy'] #strings
studentMarks = [80,70,60] #integers
data = ['Shakira',80,'Kamokya'] #mixed types

# Access the whole list
print(studentNames,type(studentNames))

# Accessing List Items
#Index(Positive indexing)
print(studentNames[0])#first item
print(studentNames[1])#second item
print(studentNames[2])#third item

#Index(Negative indexing)
print(studentNames[-3])#first item
print(studentNames[-2])#second item
print(studentNames[-1])#third item

#Appending(Adding new items to the list)
#At the end
studentNames.append('Jimia')
print(studentNames)

#At a particular position
studentNames.insert(2,'Sherina')
print(studentNames)

# print ['Edith', 'Sherina', 'Cathy]
# Add Masha at the fourth position 
#Update the name Shakira to 'Hawezi Shakira'
# Display the len of the students list
#Print all the  student names using a 'for' loop
#Calculate the total marks for the student mark variable

#answers
#(a)
names = ["Edith","Sherina","Cathy"]
for name in names:
    print(name)

   #(b) 
studentNames.insert(4,"Masha")
print(studentNames)

   #(c)
updated_name = name.replace("Shakirah","Hawezi Shakirah") 
print(updated_name)

 #(d)
studentNames=["Edith","Sherina","Cathy","Hawezi Shakirah"]
for student in studentNames:
    print(f"The length of {student} is {len(studentNames)}")

  #(e)
studentNames =["Edith","Sherina","Cathy","Hawezi Shakirah"]
for student in studentNames:
    print(studentNames)

   #(f)
studentMarks = [80,70,60]
totalMarks = sum(studentMarks)
print(f"The total marks for the students is:{totalMarks}",)
.