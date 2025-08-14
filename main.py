# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Applies the discount only if it is 20% or higher.
    
    :param price: Original price (float or int)
    :param discount_percent: Discount percentage (float or int)
    :return: Final price after discount (float)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and display final price
    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: {final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values for price and discount percentage.")
