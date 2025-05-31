# Algoritmo para cálculo da sequência de fibonacci, a sua complexidade é
# influenciada pelo fato dele ter uma recursão onde a cada execução, ele mesmo
# é chamado duas vezes, sendo assim a sua complexidade é de O(2ⁿ), pois ele é
# uma recursão em árvore binária.
def fibonacci(n: int):
    if n in (1, 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

result = fibonacci(6)
print(result)