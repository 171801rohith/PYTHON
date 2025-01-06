# Types of Inheritance


# 1. Single Inheritance
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name: {self.name}\tID: {self.id}")


class Programmer(Employee):
    def __init__(self, name, id, language="Python"):
        super().__init__(name, id)
        self.language = language

    def showDetails(self):
        super().showDetails()
        print(f"Language is {self.language}")


e = Employee("Leo Das", 420)
e.showDetails()
p = Programmer("Anthony Das", 420, "JAVA")
p.showDetails()

print("-" * 169)

# 2. Multiple Inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")


class Cricket:
    def __init__(self, role):
        self.role = role

    def show(self):
        print(f"Role: {self.role}")

class Child1(Person, Cricket):
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Child2(Cricket, Person):
    def __init__(self, name, role):
        self.name = name
        self.role = role


child1 = Child1("rohith", "batsman")
print(child1.name)
print(child1.role)
child1.show() #calls show method from 'Person' class becoz Child1 inherits Person, Cricket -> Here Person is first so
print()
child2 = Child2("gajan", "bowler")
print(child2.name)
print(child2.role)
child2.show() #calls show method from 'Cricket' class becoz Child2 inherits Cricket, Person -> Here Cricket is first so

print(Child1.mro())
print(Child2.mro())

print("-" * 169)

# 3. Multi-Level Inheritance
class GrandFather:
    def __init__(self, gfname):
        self.gfname = gfname
    
    def show(self):
        print(f"GrandFather's Name: {self.gfname}")

class Father(GrandFather):
    def __init__(self, fname, gfname):
        super().__init__(gfname)
        self.fname = fname
    
    def show(self):
        super().show()
        print(f"Father's Name: {self.fname}")

class Son(Father):
    def __init__(self, name, fname, gfname):
        super().__init__(fname, gfname)
        self.name = name

    def show(self):
        super().show()
        print(f"Son's Name: {self.name}")


son = Son("arjun", "Krishna", "Vishnu")
son.show()
print(Son.mro())

print("-" * 169)

# 4. Hybrid Inheritance
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Base):
    pass

class Derived3(Derived1, Derived2):
    pass

print("-" * 169)

# 5. Hierarchical Inheritance
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Base):
    pass