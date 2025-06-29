# Algoritmo que realiza a busca sequencial em um vetor/lista.

# `data` representa a lista ou vetor que será percorrida.
# `desire_number` representa o número a ser buscado.
def sequentialSearch(data: list, desire_number: int):
    # Variável de apoio para indicar o índice da lista de números na iteração.
    data_index = 0
    # Variável de apoio para indicar quantas vezes o algoritmo foi executado.
    steps = 0

    # Enquanto o índice for menor que o índice do último elemento da lista.
    while data_index < len(data):
        steps += 1
        # Se o elemento na iteração for igual ao número a ser buscado,
        # contabilizar um passo na quantia de vezes que o algoritmo
        # foi executado e retornar uma tupla, onde o primeiro elemento é o
        # índice do número a ser buscado e o segundo elemento é a quantia de
        # vezes que o algoritmo foi executado.
        # Caso contrário, apenas contabilizar em um o valor do índice para
        # passar para o próximo elemento e contabilizar o número de execuções
        # do algoritmo.
        if data[data_index] == desire_number:
            return (data_index, steps)
        else:
            data_index += 1
    # Caso não encontrar nada retorna -1 com o número de vezes que o algoritmo
    # foi executado.
    return (-1, steps)