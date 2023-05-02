def recursion(n):
    print(n)
    recursion(n+1)


# recursion(1)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)


# print(factorial(16))


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


# print(fibonacci(12))

def pascal_tri(n):
    pass


print(pascal_tri(8))
