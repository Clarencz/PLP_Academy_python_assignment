# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount(price,discount):
    if discount >= 20:
        return price * (1-(discount/100))
    else:
        return price
    
clothe_price = int(input("what was the tag price of your cloth? "))
discount_price = int(input("...and what was the tag discount price? "))

if discount_price >= 20:
    print(f"Surprise your cloth is selling at: {calculate_discount(clothe_price,discount_price)}")
else:
    print(f"Your cloth is selling a {clothe_price}")