# Recursion
def fact(n):
    if n == 1 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


print("Factorial is", fact(int(input("Enter a number : "))))


def akr(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akr(m - 1, 1)
    elif m > 0 and n > 0:
        return akr(m - 1, akr(m, n - 1))

print("Ackermann is", akr(int(input("Enter a m : ")), int(input("Enter a n : "))))
