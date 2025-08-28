class Circle:
    def __init__(self, r):
        self._radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if r >= 0:
            self._radius = r
        else:
            raise ValueError("Radius can not be negative!")
        
    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

c = Circle(20)
radius = c.radius
print(f"Current radius: {radius}")
area = c.area
print(f"Area : {area}")
print("---------------------")
c.radius = 40
radius = c.radius
print(f"Current radius: {radius}")
area = c.area
print(f"Area : {area}")
