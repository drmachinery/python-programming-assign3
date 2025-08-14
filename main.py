def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Args:
        price (float): Original price of the item
        discount_percent (float): Discount percentage (0-100)
    
    Returns:
        float: Final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (0-100): "))

# Calculate and display result
final_price = calculate_discount(original_price, discount_percent)

if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: ${original_price:.2f}")
    