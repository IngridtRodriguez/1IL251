def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

n=raw_input("introduzca el numero del cual quiere saber su factorial ")
print(factorial(n))
