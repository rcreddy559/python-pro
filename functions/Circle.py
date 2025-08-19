from typing import Any


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self)-> float | None | Any:
        """Calculate the area of the circle."""
        if self.radius < 0:
            return 3.14159 * (self.radius ** 2)
        return None


if __name__ == '__main__':
    c = Circle(5)
    print("Circle radius: ", c.radius)  # Output: Circle radius: 5
    print("Circle area: ", c.area())     # Output: Circle area: 78.53975
    c.radius = 10
    print("Updated Circle radius: ", c.radius)  # Output: Updated Circle radius: 10
    print("Updated Circle area: ", c.area())     # Output: Updated Circle area: 314.1595
    c2 = Circle(0)
    print("----Circle with negative radius area: ", c2.area())  # Output: Circle
    c2.radius = -15
    print("----Updated Circle radius: ", c2.radius)  # Output: Updated Circle radius: 15
