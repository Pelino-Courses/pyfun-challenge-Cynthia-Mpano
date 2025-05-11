import math

class Shape:
    """
    Base class for all geometric shapes.

    Attributes:
        name (str): The name of the shape.

    Methods:
        area(): Returns the area of the shape (to be overridden).
        perimeter(): Returns the perimeter of the shape (to be overridden).
        __str__(): Returns a human-readable description.
    """
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Shape name must be a non-empty string.")
        self.name = name.strip()

    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        return f"{self.name} (Generic Shape)"

class Circle(Shape):
    """
    Circle shape subclass.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius):
        super().__init__("Circle")
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"{self.name} with radius {self.radius:.2f}"

class Rectangle(Shape):
    """
    Rectangle shape subclass.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(self, width, height):
        super().__init__("Rectangle")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{self.name} ({self.width:.2f} * {self.height:.2f})"

class Triangle(Shape):
    """
    Triangle shape subclass.

    Attributes:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.
    """
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("The given sides do not form a valid triangle.")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"{self.name} with sides {self.a:.2f}, {self.b:.2f}, {self.c:.2f}"
