#Assignment operaters
sum = 5
sum+=6
print(sum)

#Given that we have to products a laptop and a mouse 
#Such that the price of a laptop is 300000 and the price of a mouse is 50000 
#Use a for loop the total sum of the product
Laptop = 300000
Mouse = 50000
sum = 0
product_prices = [Laptop,Mouse]
for price in product_prices:
    sum+=price
print(f"The total sum of the product is:{sum:,}")