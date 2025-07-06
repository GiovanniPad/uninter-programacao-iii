#!/usr/bin/env python


class CartaoNumerado:
    def __init__(self, numero: int, cor: str):
        self.numero = numero
        self.cor = cor
        self.proximo: CartaoNumerado | None = None

    def __repr__(self):
        return f"[{self.cor},{self.numero}]"


class ListaPaciente:
    def __init__(self):
        self.num_v = 1
        self.num_a = 201
        self.head: CartaoNumerado | None = None

    def inserirSemPrioridade(self, cartao: CartaoNumerado):
        cartao_atual = self.head

        while cartao_atual.proximo is not None:
            cartao_atual = cartao_atual.proximo

        cartao_atual.proximo = cartao

    # Inserir após todos os A e antes de todos os V
    def inserirComPrioridade(self, cartao: CartaoNumerado):
        cartao_atual = self.head

        # Se o primeiro elemento for A
        if cartao_atual.cor == "V" and cartao.cor == "A":
            cartao.proximo = self.head
            self.head = cartao
            return

        while cartao_atual.proximo is not None and cartao_atual.proximo.cor == "A":
            cartao_atual = cartao_atual.proximo

        cartao.proximo = cartao_atual.proximo
        cartao_atual.proximo = cartao

    def inserir(self):
        cor = input("Informe a cor do cartão (A/V): ").strip().upper()

        match cor:
            case "A":
                print(f"O paciente A terá o número {self.num_a}.")
                cartao = CartaoNumerado(self.num_a, cor)
                self.num_a += 1

                if self.head is None:
                    self.head = cartao
                    return

                self.inserirComPrioridade(cartao)
            case "V":
                print(f"O paciente V terá o número {self.num_v}.")
                cartao = CartaoNumerado(self.num_v, cor)
                self.num_v += 1

                if self.head is None:
                    self.head = cartao
                    return

                self.inserirSemPrioridade(cartao)
            case _:
                print("Opção inválida, retornando...")

    def imprimirListaEspera(self):
        cartao = self.head
        cartoes = []
        cartoes.append("Lista")
        while cartao is not None:
            cartoes.append(str(cartao))
            cartao = cartao.proximo
        return " -> ".join(cartoes)

    def atenderPaciente(self):
        if self.head is None:
            print("Lista de pacientes vazia, impossível atender!")
            return

        paciente_atendido = self.head
        self.head = paciente_atendido.proximo

        return paciente_atendido


def main():
    lista_pacientes = ListaPaciente()
    while True:
        print("1 - Adicionar paciente a fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")

        operacao = int(input("Escolha uma operação: ").strip())

        match operacao:
            case 1:
                lista_pacientes.inserir()
            case 2:
                print("Imprimindo a lista de pacientes...")
                pacientes = lista_pacientes.imprimirListaEspera()
                print(pacientes)
            case 3:
                paciente_atendido = lista_pacientes.atenderPaciente()
                print(
                    f"Atendendo o paciente cartão cor {paciente_atendido.cor} e número {paciente_atendido.numero}."
                )
            case 4:
                print("Encerrando")
                break
            case _:
                continue


main()
