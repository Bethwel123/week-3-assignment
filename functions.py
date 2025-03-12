def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if it is 20% or higher.
    :param price: Original price of the item (float)
    :param discount_percent: Discount percentage to be applied (float)
    :return: Final price after discount (float)
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price after discount
    final_price = calculate_discount(original_price, discount_percentage)

    print(f"The final price after discount is: Ksh{final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter valid numeric values.")
