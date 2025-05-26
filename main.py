#!/usr/bin/env python3

import random
from algorithms.binary_search import binarySearch
from algorithms.sequential_search import sequentialSearch

# Lista com 10 números inteiros aleatórios de 0 a 9.
data = random.sample(range(10), 10)

# Busca sequencial

# Imprimindo a lista desordenada para visualização.
print(data)

# Entrada do número a ser pesquisado na lista.
number = int(input("Digite o valor que deseja buscar: "))

# Executando a função de busca sequencial, passando a lista e o número a ser buscado.
# `index` representa o índice do número desejado na lista e `steps` indica a quantia
# de vezes que o algoritmo foi executado.
index, steps = sequentialSearch(data, number)

# Verificando se o valor foi encontrado ou não.
if index == -1:
    print(f"Valor não encontrado. Algoritmo executado {steps} vez(es).")
else:
    print(f"Valor encontrado na posição {index} da lista. O algoritmo foi executado {steps} vez(es).")


# Busca binária

# Para realizar a busca binária é necessário que o vetor ou lista
# esteja ordenado.
data_sorted = data.copy()
data_sorted.sort()

# Imprimindo a lista para visualização.
print(data_sorted)

# Entrada do número a ser pesquisado na lista.
number = int(input("Digite o valor que deseja buscar: "))

# Executando a função de busca binária, passando o valor inicial e final do
# índice de busca, a lista e o número a ser buscado.
# `index` representa o índice do número desejado na lista e `steps` indica a quantia
# de vezes que o algoritmo foi executado.
index, steps = binarySearch(0, len(data_sorted), data_sorted, number)

# Verificando se o número desejado foi encontrado ou não.
if index == -1:
    print(f"Valor não encontrado. Algoritmo executado {steps} vez(es).")
else:
    print(f"Valor encontrado na posição {index} da lista. O algoritmo foi executado {steps} vez(es).")
