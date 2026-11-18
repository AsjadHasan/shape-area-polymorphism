
"""Calculate areas of different shapes using OOP polymorphism."""

import math


class Shape:
    """Base class representing a geometric shape."""

    def area(self):
        """Calculate the area of a shape."""
        raise NotImplementedError("Subclasses must implement area()")


class Circle(Shape):
    """Represent a circle with a radius."""

    def __init__(self, radius):
        """Initialize the circle radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2


class Square(Shape):
    """Represent a square with a side length."""

    def __init__(self, side):
        """Initialize the square side length."""
        self.side = side

    def area(self):
        """Return the area of the square."""
        return self.side ** 2


class Triangle(Shape):
    """Represent a triangle with a base and height."""

    def __init__(self, base, height):
        """Initialize the triangle base and height."""
        self.base = base
        self.height = height

    def area(self):
        """Return the area of the triangle."""
        return 0.5 * self.base * self.height


def main():
    """Create shapes and display their calculated areas."""
    circle = Circle(7)
    square = Square(4)
    triangle = Triangle(6, 8)

    print(f"Circle area: {circle.area():.2f}")
    print(f"Square area: {square.area()}")
    print(f"Triangle area: {triangle.area()}")


if __name__ == "__main__":
    main()
