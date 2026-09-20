#Function definition and calling
print('\n')
def a():
    print("Hello world!")

a()


def greet():
    print("Hello, Anelya!")

greet()


def multiply(a, b):
    print(a * b)

multiply(4, 7)


def name(name):
    print(name)

name("Anelya")


print('\n')


#Function arguments (positional, default, *args, **kwargs)

def introduce(name, age): #positional
    print("My name is", name)
    print("I am", age, "years old")

introduce("Anelya", 18)


def fact(name  = 'Anelya'): #default
    print("I am " , name)

fact()


def add(*args): #*args
    total = 0

    for number in args:
        total += number

    print(total)

add(5, 10, 15)


def student(**kwargs): #**kwargs
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])
    print("University:", kwargs["uni"])

student(name="Anelya", age=18, uni="KBTU")


print('\n')

#Return values and statements

def square(x):
    return x * x

print(square(6))


def addition(a, b):
    return a + b

result = addition(5, 3)
print(result)


def bigger(a, b):
    if a > b:
        return a
    else:
        return b

print(bigger(7, 12))


def even(x):
    return x % 2 == 0

print(even(10))

print('\n')
#Passing lists and other data types as arguments

def numbers(nums): #list
    print(nums)

mlist = [1, 2, 3, 4, 5]

numbers(mlist)


def biggest(numbers): #biggest number
    return max(numbers)

numbers = [4, 8, 2, 10, 6]

print(biggest(numbers))


def student_info(name, age, grades): #multiple data types
    print("Name:", name)
    print("Age:", age)
    print("Grades:", grades)

student_info("Anelya", 18, [90, 85, 100])


def info(data): #tuple
    print(data)

person = ("Alex", 18, "KBTU")

info(person)

print('\n')

#Function documentation with docstrings

import functools

def lowercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().lower()
    return wrapper

@lowercase
def message():
    """Returns a message."""
    return "HELLO WORLD"

print(message())
print(message.__name__)
print(message.__doc__)

print('\n')

import functools

def double(func):
    @functools.wraps(func)
    def wrapper():
        return func() * 2
    return wrapper

@double
def number():
    """Returns a number."""
    return 5

print(number())
print(number.__name__)
print(number.__doc__)


print('\n')

import functools

def excited(func):
    @functools.wraps(func)
    def wrapper():
        return func() + "!"
    return wrapper

@excited
def greeting():
    """Returns a greeting."""
    return "Hello"

print(greeting())
print(greeting.__name__)
print(greeting.__doc__)

print('\n')

import functools

def smile(func):
    @functools.wraps(func)
    def wrapper():
        return func() + " :)"
    return wrapper

@smile
def mes():
    """Returns a message."""
    return "Good morning"

print(mes())
print(mes.__name__)
print(mes.__doc__)


#Lambda syntax and basic usage

add = lambda a, b: a + b
print(add(5, 3))


multiply = lambda a, b: a * b
print(multiply(4, 5))


square = lambda x: x ** 2
print(square(6))


even = lambda x: x % 2 == 0
print(even(10))

print('\n')


#Using lambda with map() for transformation

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print(result)


numbers = [5, 10, 15]
result = list(map(lambda x: x + 10, numbers))
print(result)


words = ["hello", "python", "world"]
result = list(map(lambda word: word.upper(), words))
print(result)


words = ["Anelya", "python", "hello"]
result = list(map(lambda word: len(word), words))
print(result)



print('\n')


#Using lambda with filter() for selection

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)


numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 != 0, numbers))
print(result)


numbers = [-5, 10, -2, 7, 0, 3]
result = list(filter(lambda x: x > 0, numbers))
print(result)


numbers = [5, 12, 8, 20, 15]
result = list(filter(lambda x: x > 10, numbers))
print(result)


print('\n')


#Using lambda with sorted() for custom sorting

numbers = [-5, 2, -10, 3]
result = sorted(numbers, key=lambda x: abs(x))
print(result)


words = ["apple", "cat", "banana", "dog"]
result = sorted(words, key=lambda word: len(word))
print(result)


students = [("Alex", 20), ("Anna", 18), ("John", 22)]
result = sorted(students, key=lambda student: student[1])
print(result)


words = ["banana", "apple", "cherry", "pear"]
result = sorted(words, key=lambda x: x[0])
print(result)

print('\n')


#Class definition and object creation

class Student:
    def hello(self):
        print("Hello!")
student1 = Student()
student1.hello()


class Car:
    def show_info(self):
        print("Toyota Camry")
        print("Year: 2022")
car1 = Car()
car1.show_info()


class University:
    def show_info(self):
        print("KBTU")
        print("Almaty, Kazakhstan")
university1 = University()
university1.show_info()


class Calculator:
    def add(self):
        print(10 + 5)
calculator1 = Calculator()
calculator1.add()

print('\n')

#The __init__() constructor method

class student:
    def __init__(self, name):
        self.name = name
student1 = student("Anelya")
print(student1.name)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Anelya", 18)
print(person1.name)
print(person1.age)


class Car:
    def __init__(self, brand):
        self.brand = brand
car1 = Car("Toyota")
print(car1.brand)


class Book:
    def __init__(self, title):
        self.title = title
book1 = Book("Harry Potter")
print(book1.title)


print('\n')

#Instance methods and the self parameter

class student:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print("My name is", self.name)
student1 = student("Anelya")
student1.say_name()



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)
rectangle1 = Rectangle(5, 10)
rectangle1.area()


class Car:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)
car1 = Car("Toyota")
car1.show_brand()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(self.name, "is", self.age, "years old")
person1 = Person("Anleya", 18)
person1.introduce()


#Class variables vs instance variables

class Student:
    university = "KBTU"

    def __init__(self, name):
        self.name = name
student1 = Student("Anelya")
student2 = Student("Alina")
print(student1.university)
print(student2.university)
print(student1.name)
print(student2.name)

print('\n')
class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand
car1 = Car("Toyota")
car2 = Car("BMW")
print(car1.wheels)
print(car2.wheels)
print(car1.brand)
print(car2.brand)

print('\n')
class University:
    country = "Kazakhstan"

    def __init__(self, name):
        self.name = name

uni1 = University("KBTU")
uni2 = University("Nazarbayev University")
print(uni1.country)
print(uni2.country)
print(uni1.name)
print(uni2.name)

print('\n')

class Animal:
    legs = 4

    def __init__(self, name):
        self.name = name
animal1 = Animal("Cat")
animal2 = Animal("Dog")
print(animal1.legs)
print(animal2.legs)
print(animal1.name)
print(animal2.name)

print('\n')

#Modifying and deleting object properties

class Product: #modify
    def __init__(self, price):
        self.price = price
product1 = Product(10000)
print(product1.price)
product1.price = 15000
print(product1.price)


class Student: #delete
    def __init__(self, name):
        self.name = name
student1 = Student("Anelya")
print(student1.name)
del student1.name


class Person: #modify
    def __init__(self, age):
        self.age = age
person1 = Person(18)
print(person1.age)
person1.age = 19
print(person1.age)


class Car: #delete
    def __init__(self, brand):
        self.brand = brand
car1 = Car("Toyota")
print(car1.brand)
del car1.brand


print('\n')

#Parent and child class relationships

class Person:              # parent
    def speak(self):
        print("Hello")

class Student(Person):     # child
    def study(self):
        print("studying")

student = Student()
student.speak()
student.study()

print('\n')

class Student:                    # parent
    def study(self):
        print("studying")

class UniversityStudent(Student): # child
    def attend_class(self):
        print("attending class")
student = UniversityStudent()
student.study()
student.attend_class()

print('\n')
class Employee:              #parent
    def work(self):
        print("working")
class Programmer(Employee):  #child
    def code(self):
        print("coding")
programmer = Programmer()
programmer.work()
programmer.code()

print('\n')
class Computer:               #parent
    def start(self):
        print("Starting")

class Laptop(Computer):       #child
    def close(self):
        print("Closing laptop")
laptop = Laptop()
laptop.start()
laptop.close()

print('\n')

#Using super() to call parent methods

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
student = Student("Anelya")
print(student.name)

print('\n')

class Book:
    def __init__(self, title):
        self.title = title
class Novel(Book):
    def __init__(self, title):
        super().__init__(title)
novel = Novel("Harry Potter")
print(novel.title)


print('\n')

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
student = Student("Anelya", 18)
print(student.name)
print(student.age)


print('\n')

class Phone:
    def __init__(self, model):
        self.model = model
class Smartphone(Phone):
    def __init__(self, model):
        super().__init__(model)
phone = Smartphone("iPhone")
print(phone.model)

print('\n')


#Method overriding

class Person:
    def hello(self):
        print("Hello")
class Student(Person):
    def hello(self):
        print("I am a student")
student = Student()
student.hello()

print('\n')

class Employee:
    def work(self):
        print("Working")
class Manager(Employee):
    def work(self):
        print("Managing")
manager = Manager()
manager.work()

print('\n')

class Game:
    def start(self):
        print("Game started")
class Minecraft(Game):
    def start(self):
        print("Minecraft started")
game = Minecraft()
game.start()

print('\n')

class Student:
    def introduce(self):
        print("I am a student")
class GraduateStudent(Student):
    def introduce(self):
        print("I am a graduate student")
student = GraduateStudent()
student.introduce()

print('\n')


#Multiple inheritance 

class Student:
    def study(self):
        print("Studying")
class Athlete:
    def train(self):
        print("Training")
class StudentAthlete(Student, Athlete):
    pass
person = StudentAthlete()
person.study()
person.train()

print('\n')

class Writer:
    def write(self):
        print("Writing")
class Artist:
    def draw(self):
        print("Drawing")
class ContentCreator(Writer, Artist):
    pass
creator = ContentCreator()
creator.write()
creator.draw()

print('\n')


class Developer:
    def code(self):
        print("Coding")
class Designer:
    def design(self):
        print("Designing")
class WebDeveloper(Developer, Designer):
    pass
person = WebDeveloper()
person.code()
person.design()

print('\n')


class Employee:
    def work(self):
        print("Working")
class Student:
    def study(self):
        print("Studying")
class Intern(Employee, Student):
    pass
intern = Intern()
intern.work()
intern.study()

print('\n')


