class Strings:
    def GetString(self):
        self.text = input("Enter your text: ")

    def printString(self):
        print(self.text.upper())
obj = Strings()
obj.GetString()
obj.printString()


class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __innit__(self, length):
        self.length = length

    def area(self):
        print(self.length * self.length)

square = Square(5)
square.area()

class Rectangle:
    def __innit__(self, length, width):
        self.length = length
        self.width = width 
    def area(self):
        print(self.width * self.length)
rectangle = Rectangle(5, 3)
rectangle.area()



import math 

class Point:
    def __innit__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The x is {self.x}, the y is {self.y}")

    def move (self, x, y):
        self.x = x
        self.y = y

    def dist (self, other):
        return math.sqrt((self.x - other.x)**2 +(self.y - other.y)**2)

p1 = Point(0, 0)
p2 = Point(3, 4)
p1.show()
p1.move(10, 20)
print(p1.dist(p2))
p1.show()




class Account:
    def __innit__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance 

    def deposit(self, amount) :
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.deposit :
            self.deposit -= amount
            print("Withdrawal successful")
        else:
            print("Not enough")

account = Account("Anelya", 1800)
account.deposit(500)
account.deposit(200)
print(account.balance())

account.withdraw(100)
print(account.balance())
account.withdraw(500)
print(account.balance())



def is_prime(n):
    if n<2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4 , 5 , 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(), numbers))
print(prime_numbers)



def grams_to_ounces(n):
    return n * 28.3495231
grams = grams_to_ounces(3)
print(grams)



def solve(numlegs, numheads) :
    rabbits = (numlegs - 2*numheads)//2 
    chickens = numheads - rabbits
    return rabbits, chickens

chickens, rabbits = solve(34, 78)
print(chickens)
print(rabbits)


def is_primee(n):
    if n<2:
        return False
    for i in range (2, int (n**0.5)+1):
        if(n%i ==0):
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_primee(n)]

numbers = list(map(int, input().split()))
print(filter_prime(numbers))


from itertools import permutations

def print_permutations(text):
    for p in permutations(text):
        print(",".join(p))
text = input()
print(print_permutations(text))



def reverse_words(sentence):
    words = sentence.split()
    words.reverse()

    return (",".join(words))

sentence = input()
print(reverse_words(sentence))