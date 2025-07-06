#!/usr/bin/env python


class Estado:
    def __init__(self, sigla: str, nomeEstado: str) -> None:
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

    def __repr__(self) -> str:
        return self.sigla


class ListaEstado:
    def __init__(self):
        self.head = None

    # Impressão da tabela hash!!!
    def __repr__(self) -> str:
        estado = self.head
        estados = []
        while estado is not None:
            estados.append(str(estado))
            estado = estado.proximo
        estados.append("None")

        return "->".join(estados)

    def inserirEstado(self, estado: Estado) -> None:
        if self.head is None:
            self.head = estado
            return

        estado.proximo = self.head
        self.head = estado


def funcao_hash(chave: str, n: int) -> str:
    if chave == "DF":
        return 7

    posicao = (ord(chave[0]) + ord(chave[1])) % n

    return posicao


def inserirEstadosTabela():
    estados = {
        "AC": "Acre",
        "AL": "Alagoas",
        "AP": "Amapá",
        "AM": "Amazonas",
        "BA": "Bahia",
        "CE": "Ceará",
        "DF": "Distrito Federal",
        "ES": "Espírito Santo",
        "GO": "Goiás",
        "MA": "Maranhão",
        "MT": "Mato Grosso",
        "MS": "Mato Grosso do Sul",
        "MG": "Minas Gerais",
        "PA": "Pará",
        "PB": "Paraíba",
        "PR": "Paraná",
        "PE": "Pernambuco",
        "PI": "Piauí",
        "RJ": "Rio de Janeiro",
        "RN": "Rio Grande do Norte",
        "RS": "Rio Grande do Sul",
        "RO": "Rondônia",
        "RR": "Roraima",
        "SC": "Santa Catarina",
        "SP": "São Paulo",
        "SE": "Sergipe",
        "TO": "Tocantins",
    }

    for sigla, nomeEstado in estados.items():
        posicao = funcao_hash(sigla, n)
        estado = Estado(sigla, nomeEstado)
        if tabela[posicao] is None:
            lista_estados = ListaEstado()
            lista_estados.inserirEstado(estado)
            tabela[posicao] = lista_estados
        else:
            lista: ListaEstado = tabela[posicao]
            lista.inserirEstado(estado)


def inserirEstudanteTabela():
    eu = ["GP", "Giovanni Padilha"]
    posicao = funcao_hash(eu[0], n)
    estado = Estado(sigla=eu[0], nomeEstado=eu[1])
    lista = tabela[posicao]
    lista.inserirEstado(estado)


def exibirTabela():
    i = 0
    for lista in tabela:
        print(f"{i}: {lista}")
        i += 1


n = 10
tabela: list[ListaEstado | None] = [None] * n


def main():
    exibirTabela()

    print("----------------------------------------")

    inserirEstadosTabela()
    exibirTabela()

    print("----------------------------------------")

    inserirEstudanteTabela()
    exibirTabela()


main()
