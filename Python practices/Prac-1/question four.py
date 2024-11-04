
#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.
# def updated_food_list():

#    favourite_foods = ["Pizza","burger","pasta","sushi","ice cream"]
#    favourite_foods.append("tacos")
#    favourite_foods.append("salad")
#    favourite_foods.remove("sushi")

#    print(f"updated favourite foodslist:",favourite_foods) 

# updated_food_list()




#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.
def list_numbers():
   numbers = [2,5,8,10,3,6]
   print(numbers[0])
   print(numbers[5])
   print(numbers[::-1])
   sum = 0
   for elements in numbers:
    sum+=elements
   print(f"The sum of the elements is:{sum:,}")
list_numbers()