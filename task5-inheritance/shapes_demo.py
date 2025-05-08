from shapes import Circle, Rectangle, Triangle

def main():
    print("=== Geometric Shape Calculator ===")

    while True:
        print("\nChoose a shape:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        try:
            if choice == "1":
                radius = float(input("Enter radius of the circle: "))
                shape = Circle(radius)

            elif choice == "2":
                width = float(input("Enter width of the rectangle: "))
                height = float(input("Enter height of the rectangle: "))
                shape = Rectangle(width, height)

            elif choice == "3":
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                c = float(input("Enter side c: "))
                shape = Triangle(a, b, c)

            elif choice == "4":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please select a valid option.")
                continue

            # Display results
            print("\nShape Details:")
            print(shape)
            print(f"Area: {shape.area():.2f}")
            print(f"Perimeter: {shape.perimeter():.2f}")

        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()