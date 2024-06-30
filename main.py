# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        return Vector(*(x + y for x, y in zip(self.components, other.components)))

    def __sub__(self, other):
        return Vector(*(x - y for x, y in zip(self.components, other.components)))

    def dot(self, other):
        return sum(x * y for x, y in zip(self.components, other.components))

    def norm(self):
        return sum(x**2 for x in self.components) ** 0.5


    def distance(self, other):
        diff = self.__sub__(other)
        return diff.norm()
