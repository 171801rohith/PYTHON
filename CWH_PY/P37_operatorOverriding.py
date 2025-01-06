# Operator Overriding
# Dunder Methods


class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"({self.i})i + ({self.j})j + ({self.k})k"

    def __add__(self, obj):
        return Vector(self.i + obj.i, self.j + obj.j, self.k + obj.k)

    def __sub__(self, obj):
        return Vector(self.i - obj.i, self.j - obj.j, self.k - obj.k)

    def __mul__(self, obj):
        return Vector(self.i * obj.i, self.j * obj.j, self.k * obj.k)


v1 = Vector(3, 3, 4)
print(v1)
# print(dir(v1))

v2 = Vector(7, 5, 1)
print(v2)

v3 = v1 + v2  # '+' -> calls '__add__'
print(v3) 
print(type(v3))

v4 = v1 - v2  # '-' -> calls '__sub__'
print(v4) 

v5 = v1 * v2  # '*' -> calls '__mul__'
print(v5) 
