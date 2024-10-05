def fibonacci(n):
    a, b = 0, 1
    i = 0
    while i < n:
        print(a, end=" ")
        a, b = b, a + b
        i += 1

n = int(input("Informe a sequência desejada: "))
fibonacci(n)