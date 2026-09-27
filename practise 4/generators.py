#1

def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

for x in squares(5):
    print(x)


#2 
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
print(",".join(map(str, even_numbers(n))))


#3 
def numbers(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for number in numbers(n):
    print(number)

#4
def squares4(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input())
b = int(input())

for number in squares4(a, b):
    print(number)

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())

for number in countdown(n):
    print(number)