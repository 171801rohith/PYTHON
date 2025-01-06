# Method OverRiding

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"My name is {self.name}, I'm an animal."
    
class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound
    
    def speak(self):
        return f"My name is {self.name}, I'm a dog and I {self.sound}."

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound
    
    def speak(self):
        return f"My name is {self.name}, I'm a cat and I {self.sound}."
    

a = Animal("Lion")
print(a.speak())

d = Dog("Buddy", "Bark")
print(d.speak())

c = Cat("Tom", "Meow")
print(c.speak())

