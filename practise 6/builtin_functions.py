numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x**2, numbers))
print("Square:", squared)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even:", evens)


from functools import reduce
numbers = [1, 2, 3, 4, 5]

total_sum = reduce(lambda x, y: x + y, numbers)
product = reduce(lambda x, y: x * y, numbers)

print("Sum:", total_sum)
print("Multiplication:", product)


names = ["Anne", "Victor", "Jake"]
scores = [85, 92, 78]

for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

print("\nUse zip:")
for name, score in zip(names, scores):
    print(f"Student {name} got {score} points.")


val_str = "123"
val_float = 45.67

print(type(val_str))
print(isinstance(val_float, float))

num_int = int(val_str)
num_str = str(val_float)

print(num_int * 2)
print(num_str + " is a string now")

