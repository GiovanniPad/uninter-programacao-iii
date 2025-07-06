# Algoritmo que contém apenas um laço único, sendo assim é O(n).
def exercicio1(dados):
    for i in range(0, len(dados) / 2, 1):
        dados[i] = i * 2


# Algoritmo que contém dois laços independentes em sequência, por
# nenhum deles ter dependência um no outro a complexidade é O(n).
def exercicio2(dados):
    for i in range(0, len(dados), 1):
        dados[i] = i + 1
    for i in range(0, len(dados), 1):
        dados[i] = i - 1


# Algoritmo que contém dois laços, e o laço interno possui dependência
# no laço externo, neste caso, os laços possui uma execução constante,
# ou seja, a quantidade de execuções sempre vai constante até o fim.
# Por isso O(n²).
def exercicio3(dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
            dados[i] = dados[i] + 1


# Neste caso, há três laços aninhados, sendo assim a complexidade é O(n²).
# Pois, por mais que há três laços, o último laço interno possui um número
# fixo de execuções (9 milhões), não dependendo do tamanho do conjunto
# de dados.
def exercicio4(dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
            for k in range(0, 9000000, 1):
                dados[i] = dados[j] + 1
