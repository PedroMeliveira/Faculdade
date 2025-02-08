def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def count_calls(n, calls=[0]):
    calls[0] += 1  # Contabiliza cada chamada da função
    if n == 0 or n == 1:
        return 1
    return count_calls(n-1, calls) + count_calls(n-2, calls)

n = 5  # Número de Fibonacci desejado
calls = [0]  # Contador de chamadas
fib_value = count_calls(n, calls)  # Calcula Fibonacci e conta chamadas

print(f"Fibonacci({n}) = {fib_value}")
print(f"Número de chamadas recursivas: {calls[0]}")
