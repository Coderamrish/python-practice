# A generator is a function that returns an iterator using the yield keyword instead of return. It allows lazy evaluation, meaning values are generated on the fly instead of storing them in memory.
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))  # 🔹 Output: 1
print(next(gen))  # 🔹 Output: 2
print(next(gen))  # 🔹 Output: 3
# print(next(gen))  # ❌ Throws StopIteration (No more values)
#  Generator for Fibonacci Sequence
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(7):
    print(num, end=" ")

# Just like list comprehensions, we can create generators in a single line:
gen_exp = (x * x for x in range(5))

print(next(gen_exp))  # 🔹 Output: 0
print(next(gen_exp))  # 🔹 Output: 1
print(next(gen_exp))  # 🔹 Output: 4
