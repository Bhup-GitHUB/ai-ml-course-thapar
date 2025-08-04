# 11. Classes and Objects
# Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print("Area:", rect.calculate_area())
print("Perimeter:", rect.calculate_perimeter())

# Student class
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades)

student = Student("John", 19, [70, 80, 90])
student.display_details()

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

animal = Animal("Generic Animal")
animal.speak() # Output: Generic animal sound

dog = Dog("Buddy")
dog.speak()    # Output: Woof!


