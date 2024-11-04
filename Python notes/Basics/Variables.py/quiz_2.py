#Write a program that takes two numbers as input and displays their sum, product, difference and their qoutient
# we either cast the value to an integer or a float
num_one = int(input('enter number 1'))
num_two = int(input('enter number 2'))
sum = num_one + num_two
print(f"the sum of {num_one} and {num_two} is :{sum}") 

difference = num_two - num_one
print(f"the difference of {num_two} and {num_one} is :{difference}")

product = (num_two * num_one)
print(f"the product of {num_one} and {num_two} is :{product}")

qoutient =num_two / num_one
print(f"the qoutient of {num_two} and {num_one} is :{qoutient}")

floor_division = num_one//num_two
print(f"the floor_division of {num_two} and {num_one} is :{floor_division}")

modulus =num_one % num_two
print(f"the modulus of {num_one} and {num_two} is :{modulus}")

# Write a program that compares two integers and prints whether the first number is greater than, less than or equal to the second number
if num_one>num_two :
    print(f"{num_one} is greator than {num_two}")
elif num_one<num_two :
    print(f"{num_one} is less than {num_two} ")
else :
    print(f"they are equal")

# Write a program that check if a given no is between 10 and 20 (20 is inclusive) using logical operators
given_number = int(input("enter the given_number"))
if 10 < given_number <= 20 :
    print(f"{given_number}is between")
    print(f"{given_number}is not between")

#Write a program that prints the squares of all integers from 1-10 using a 'for' loop
for integers in range(1,11):
    print(f"The square of{integers}is: {integers**2} ")

# Write a simple program that asks the user for their age "if their age is >= than 18"you are adult qualified,
Age = int(input("enter the age"))
if Age>=18:
    print("your an adult")
else:
    print("your not adult qualified")

    
#we have the following student details and marks enter these details from the keyboard
#studentName = Ritah Liz
#studentNumber = SEP23/BCS/14
#programmimg = 78
#DataScience = 89
#CompApplication=55
#qn; calculate the average mark and print the ans in 3dps
student_name = input("Enter your student name :")
student_number = input("Enter your student number :")
programming = int(input("Enter your programming mark:"))
data_science = int(input("Enter your data science mark :"))
comp_applications = int(input("Enter your comp applications mark :"))
sum = programming + data_science + comp_applications
number_of_subjects = 3
average = round((sum/number_of_subjects),3)
print(f"average of {student_name} and number is {student_number} and average is: {average}")


#2 Write  a program that converts celcius to fahrenheit .The program should should ask the user to enter the temp in degrees celsius and the display the temp converted to fahrenheit degrees
celcius = int(input("/\nEnter temperature in celcuis degrees"))
fahrenheit = (celcius *1.8)+32
print(f"{celcius} degree celcius is egual to {fahrenheit} degree fahrenheit", end="\n\n")

#3 A car's mile per gallon can be calculated with  the following formula (MPG=MilesDriven/gallons of gas used) .
#Write a program that asks a user for the number of miles driven and gallons used. 
#It should calculate the car's miles per gallons used and display the result
mile_driven = float(input("\nenter the number of miles"))
gallons_of_gas_used = float(input("enter the gallons of gas used"))
MPG = mile_driven/gallons_of_gas_used
print("A cars mile per gallon=",MPG,end="\n\n")
