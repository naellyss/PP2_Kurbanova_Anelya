#Boolean Values
print(7 > 4)
print(7==7)
print(7<5)
print(8>0)
print(9<5)

print("\n")

#Booleans as Comparison Results
x = 6
y = 24

if x > y:
  print("x is greater than y")
else:
  print("x is not greater than y")



age = 17

if age >= 18:
    print("you are an adult")
else:
    print("you are not an adult")



a = 7
b = 7

same = a == b

print(same)


number = 8
even = number % 2 == 0
print(even)

number2  = 4
odd = number %2 != 0
print(odd)

print("\n")

#Boolean Operators
x = 10
y = 20
result = x > 5 and y > 15
print(result)

x = 5
y = 15
result = x > 10 or y > 10
print(result)

age = 16
result = age < 12 or age > 57
print(result)

raining = True
result = not raining
print(result)

age = 18
student = True
result = age > 17 and student == True
print(result)

print("\n")


#If Statement
x = 10
if x > 5:
    print("x is greater than 5")

number = 8
if number % 2 == 0:
    print("the number is even")

n = -3
if n < 0:
    print("the n is negative")

age = 20
if age >= 18:
    print("you are legal")

m = 3
if m < 5:
    print("m is smaller than 5")

print("\n")

#If Else
x = 10
y = 20
if x > y:
    print("x is greater")
else:
    print("y is greater")

money = 3000
price = 5000
if money >= price:
    print("you can buy it")
else:
    print("not enough")

a = 10
b = 10
if a == b:
    print("they are equal")
else:
    print("they are different")



x = 25
if x < 30:
    print("small")
else:
    print("large")


number = -4
if number > 0:
    print("positive")
else:
    print("not positive")

print("\n")

#If Elif Else

num = 0
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")



x = 10
y = 10
if x > y:
    print("x is greater")
elif x < y:
    print("y is greater")
else:
    print("equal")


age = 56
if age < 12:
    print("kid")
elif age < 18:
    print("teen")
else:
    print("adult")



a = 7
if a == 0:
    print("zero")
elif a % 2 == 0:
    print("even")
else:
    print("odd")