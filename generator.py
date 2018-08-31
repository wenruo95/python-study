import sys


li = [4,5,6]
it = iter(li)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("iter->exit")
        break

print("\n\n----------\n\n")

def fibonacci(n):
    a, b, counter = 1, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)

while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()

