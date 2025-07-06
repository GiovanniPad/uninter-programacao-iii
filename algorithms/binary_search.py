# Algoritmo que realiza a busca binária em um vetor/lista.

# `start` é o índice inicial e `end` é o índice final.
# `data` é a lista de números inteiros ordenados.
# `desire_number` é o número que é para ser buscado.
def binarySearch(start: int, end: int, data: list, desired_number: int):
    # Variável para contar o número de vezes que o algoritmo foi executado.
    steps = 0

    # Enquanto o índice inicial for menor que o índice final o loop executa.
    # Isso é garante que os "ponteiros" não vão ter se cruzado e a busca vai
    # sempre iniciar de um índice menor que o final.
    while start <= end:
        steps += 1
        # Encontrando o índice do elemento central.
        middle = (start + end) // 2

        # Se o número buscado for maior que o elemento central da sequência,
        # o valor inicial é substituído pelo índice do elemento central com
        # o acréscimo do valor 1. Indica que o número buscado é maior que o
        # elemento central, descartando os elementos anteriores.
        # Se o número buscado for menor que o elemento central da sequência,
        # o valor final é substituído pelo índice do elemento central com o
        # decréscimo do valor 1. Indica que o número buscado é menor que o
        # elemento central, descartando todos os elementos seguintes.
        # Caso contrário, retorna uma tupla contendo o índice do número
        # encontrado e o número de vezes que o algoritmo foi executado. Neste
        # caso, o número buscado foi encontrado.

        # Ao realizar essas operações, o número de elementos a ser buscado é
        # cortado ao meio toda vez, descartando muitos elementos e melhorando
        # a eficiência da busca.
        if desired_number > data[middle]:
            start = middle + 1
        elif desired_number < data[middle]:
            end = middle - 1
        else:
            return (middle, steps)

    # Caso não encontrar o número retorna -1 com o número de execuções do algoritmo.
    return (-1, steps)
