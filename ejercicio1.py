import time

# Función recursiva para Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Función iterativa para Fibonacci
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Función recursiva para Factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Función iterativa para Factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Función para medir el tiempo de ejecución
def measure_time(func, n):
    start_time = time.time()
    func(n)
    return time.time() - start_time

# Valores de n para probar
n_values = [10, 20, 30, 40, 50]

# Medición de tiempo para Fibonacci
print("Tiempo de ejecución para Fibonacci:")
for n in n_values:
    time_recursive = measure_time(fibonacci_recursive, n)
    time_iterative = measure_time(fibonacci_iterative, n)
    print(f"n={n}: Recursivo={time_recursive:.6f}s, Iterativo={time_iterative:.6f}s")

# Medición de tiempo para Factorial
print("\nTiempo de ejecución para Factorial:")
for n in n_values:
    time_recursive = measure_time(factorial_recursive, n)
    time_iterative = measure_time(factorial_iterative, n)
    print(f"n={n}: Recursivo={time_recursive:.6f}s, Iterativo={time_iterative:.6f}s")