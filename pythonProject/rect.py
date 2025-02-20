class Rectangle:
    def __init__(self, length, width, unit_cost=0):
        self.length = length
        self.width = width
        self.unit_cost = unit_cost

    def get_area(self):
        return self.length * self.width

    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost


r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s sq units" % (r.get_area()))