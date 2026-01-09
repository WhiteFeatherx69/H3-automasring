def Fibonacci(n):
    fib_liste = []
    if n <= 0:
        return fib_liste
    fib_liste.append(0)
    if n >= 2:
        fib_liste.append(1)
    for i in range(2, n):
        next_fib = fib_liste[i-1] + fib_liste[i-2]
        fib_liste.append(next_fib)
    return fib_liste

n = 10
resultat = Fibonacci(n)
print(resultat)