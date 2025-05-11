# inventory_demo.py

from product import Product

def main():
    try:
        # Get user input for product details
        name = input("Enter product name: ").strip()
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        product = Product(name, price, quantity)
        product.display_info()

        while True:
            print("\nWhat would you like to do?")
            print("1. Add inventory")
            print("2. Remove inventory")
            print("3. View product info")
            print("4. Exit")

            choice = input("Choose an option (1-4): ").strip()

            if choice == "1":
                amount = int(input("Enter amount to add: "))
                product.add_inventory(amount)

            elif choice == "2":
                amount = int(input("Enter amount to remove: "))
                product.remove_inventory(amount)

            elif choice == "3":
                product.display_info()

            elif choice == "4":
                print("Exiting inventory system.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

    except ValueError as e:
        print("Input Error:", e)

if __name__ == "__main__":
    main()
