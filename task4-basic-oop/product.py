class Product:
    """
    A class to represent a product in an inventory system.

    Attributes:
        name (str): The name of the product.
        price (float): The price of a single unit of the product. Must be non-negative.
        quantity (int): The quantity of the product in stock. Must be non-negative.

    Methods:
        add_inventory(amount): Adds to the product's inventory.
        remove_inventory(amount): Removes from the product's inventory.
        total_value(): Returns the total value (price * quantity).
        display_info(): Prints the product's details.
    """

    def __init__(self, name: str, price: float, quantity: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must be a non-empty string.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name.strip()
        self.price = float(price)
        self.quantity = int(quantity)

    def add_inventory(self, amount: int):
        """
        Adds a specified amount to the inventory.

        Args:
            amount (int): The amount to add. Must be positive.

        Raises:
            ValueError: If amount is not a positive integer.
        """
        if amount <= 0:
            raise ValueError("Add amount must be positive.")
        self.quantity += amount
        print(f"{amount} units added to '{self.name}'. New quantity: {self.quantity}")

    def remove_inventory(self, amount: int):
        """
        Removes a specified amount from the inventory.

        Args:
            amount (int): The amount to remove. Must be positive and not more than available quantity.

        Raises:
            ValueError: If amount is not valid.
        """
        if amount <= 0:
            raise ValueError("Remove amount must be positive.")
        if amount > self.quantity:
            raise ValueError("Cannot remove more than available quantity.")
        self.quantity -= amount
        print(f"{amount} units removed from '{self.name}'. New quantity: {self.quantity}")

    def total_value(self) -> float:
        """
        Calculates the total value of the product inventory.

        Returns:
            float: Total value (price * quantity)
        """
        return self.price * self.quantity

    def display_info(self):
        """
        Displays information about the product.
        """
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: ${self.total_value():.2f}")
