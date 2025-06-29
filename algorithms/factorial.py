# Neste algoritmo há o cálculo de valores fatoriais, sua complexidade
# é influenciada pela recursividade que ele apresenta de que, a cada chamada
# do algoritmo, ele chama ele mesmo uma vez. Sendo assim a complexidade é de
# O(n).
def factorial(n: int):
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)

