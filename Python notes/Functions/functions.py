#Function is always used in programming to perform a particular tasks
#incase when there is no function name we use pass
#argument are values passed in function
#parameters acts as the data/information(variable)
#create a functin that returns the main components of functions, the output should say main
def function_basics():
 print(f'The main components of functions are function body, parameters and argument')
function_basics()

#create a function that returns your student_name ,registration_number and student_age
def student_details():
    student_name = "Kideni Jimia"
    student_age = 20
    registration_number = "2024/DSC/0041/SS"
    print(f'My name is {student_name}, with registration number {registration_number} and am {student_age} years old')
student_details()    

#Parametrs
#Create a function that returns your  student_name ,registration_number and student_age as parametrs
def student_details_parameters(name ,age,reg_no):
    print(f'My name is {name} and am {age} years old with Reg No. {reg_no}')
student_details_parameters('Jimia',20,'2024/DSC/0041/SS')    
    
#Return values(instead of print we can use return)
def my_name():
    return"Jimia" 
my_name()  
#View Output
name = my_name()
print(name)

#Approach 2
def myAge():
    age= 20
    return age

print(f'Am {myAge()} years old ')

#or
def myNameParameter(name):
    return name
myNameParameter('Jimia')

#Create a function that calculate the area of a triangle ,the base and height must be function parameters
def area_of_a_triangle(base,height):
    area = (1/2) * base * height
    print(f'The Area of a triangle with base{base} and height {height} is : {area}')
area_of_a_triangle(6,7)  

#Approach 2
def area_of_a_triangle():
    base = int(input("Enter the base\t:"))
    height = int(input("Enter the height\t:"))
    area = int ((1/2)* base * height)
    print(f'The Area of a triangle with base{base} and height {height} is : {area}')
area_of_a_triangle()