def calcula_fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib


def pertence():
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

    if numero in calcula_fibonacci(numero):
        print("O número pertence à sequência de Fibonacci.")
    else:
        print("O número não pertence à sequência de Fibonacci.")
