import random

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Error: Please enter a valid numeric value.")

def main():
    products = ["Fertilizer", "Pesticides", "Seeds", "Animal Feed", "Gardening Tools", "Irrigation Equipment"]
    product1 = random.choice(products)
    product2 = random.choice(products)

    print(f"Please enter the details for {product1}:")
    original_price1 = get_valid_input("Enter the original price: ")
    discount_percent1 = get_valid_input("Enter the discount percentage (should be >= 20): ")

    print(f"Please enter the details for {product2}:")
    original_price2 = get_valid_input("Enter the original price: ")
    discount_percent2 = get_valid_input("Enter the discount percentage (should be >= 20): ")

    final_price1 = calculate_discount(original_price1, discount_percent1)
    final_price2 = calculate_discount(original_price2, discount_percent2)

    print(f"Final price of {product1}: ${final_price1:.2f}")
    print(f"Final price of {product2}: ${final_price2:.2f}")

if __name__ == "__main__":
    main()
