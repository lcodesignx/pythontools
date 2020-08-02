#!/usr/local/bin/python3 

fibonacci_cache = {}

def fibonacci(n):

    # if value is cached, return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # cache the falue and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 101):
    print(n, ":", fibonacci(n))
