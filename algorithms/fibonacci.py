def fibonacci(n: int):
    if n in (1, 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

result = fibonacci(6)
print(result)