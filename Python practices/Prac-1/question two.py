# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and send their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 
def calculate_bmi():
    weight = int(input("\nEnter the weight in kilograms: "))
    height = int(input("\nEnter the height in meters: "))
    BMI = weight/height
    if BMI < 18.5:
        print("underweight")
    elif 18.5 >= BMI >=24.9:
        print("Normal weight")
    elif 25 >= BMI >= 29.9:
        print("over weight")
    else:
        print("obesse") 
calculate_bmi()






# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# # achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)
def volume_of_a_cylinder():
     r =int(input("Enter the raduis of the cylinder:\n "))
     h = int(input("Enter the height of the cylinder:\n "))
     import math
     pie = math.pi
     V = pie * r**2 * h
     print(f"The volume of a cylinder with r={r} and h={h} is {V:}")
volume_of_a_cylinder()