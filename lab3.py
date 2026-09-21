import math

#task 1
class StringProcessor:
    def __init__(self):
        self.user_string = ""

    def getString(self):
        self.user_string = input("Enter a string: ")

    def printString(self):
        print(self.user_string.upper())


#task 2
class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length ** 2)



#task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width



#task 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)



#task 5
class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal denied. Requested: {amount}, Available: {self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

acc = Account("John", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(150)  



#task 6
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 20]
prime_numbers = list(filter(lambda x: prime(x), numbers))
print("Prime numbers:", prime_numbers)

print("\n")

#Python Function

import math
import itertools
import random

#task 1
def grams_to_ounces(grams):
    return grams / 28.3495231



#task 2
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)




#task 3
def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None, None



#task 4
def filter_prime(numbers):
    def is_p(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [num for num in numbers if is_p(num)]



#task 5
def print_permutations(s):
    perms = [''.join(p) for p in itertools.permutations(s)]
    print("\n".join(perms))



#task 6
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])



#task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False



#task 8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False



#task 9
def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)



#task 10
def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result



#task 11
def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]



#task 12
def histogram(lst):
    for val in lst:
        print('*' * val)



#task 13
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    secret_number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    guesses_taken = 0
    while True:
        print("Take a guess.")
        try:
            guess = int(input())
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        guesses_taken += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"\nGood job, {name}! You guessed my number in {guesses_taken} guesses!")
            break



from lab3 import (
    grams_to_ounces,
    fahrenheit_to_celsius,
    reverse_words,
    has_33,
    spy_game
)

print("100 grams in ounces:", grams_to_ounces(100))
print("98.6°F in Celsius:", fahrenheit_to_celsius(98.6))
print("Reversed sentence:", reverse_words("We are ready"))
print("has_33([1, 3, 3]):", has_33([1, 3, 3]))
print("spy_game([1,0,2,4,0,5,7]):", spy_game([1, 0, 2, 4, 0, 5, 7]))



movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

#task 1
def is_above_5_5(movie):
    return movie["imdb"] > 5.5

#task 2
def high_score_movies(movie_list):
    return [m for m in movie_list if is_above_5_5(m)]

#task 3
def movies_by_category(movie_list, category):
    return [m for m in movie_list if m["category"].lower() == category.lower()]

#task 4
def average_imdb(movie_list):
    if not movie_list:
        return 0.0
    return sum(m["imdb"] for m in movie_list) / len(movie_list)

#task 5
def average_imdb_by_category(movie_list, category):
    filtered = movies_by_category(movie_list, category)
    return average_imdb(filtered)


print(is_above_5_5(movies[2]))

print(len(high_score_movies(movies)))

print([m["name"] for m in movies_by_category(movies, "Romance")])

print(average_imdb(movies))

print(average_imdb_by_category(movies, "Romance"))