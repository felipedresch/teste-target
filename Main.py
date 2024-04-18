from Ex1 import ex1
from Ex2 import pertence
from Ex5 import reverter_string


def main():
    opcao = int(input("Digite o número do exercício desejado: "))

    match opcao:
        case 1:
            print("Ex1")
            ex1()
        case 2:
            print("Ex2")
            pertence()
        case 3:
            print("Ex3\nSequência de elementos:")
            print("A- 9\nB- 128\nC- 49\nD- 100\nE- 13\nF- 20")
        case 4:
            print("Resposta enviada no teste")
        case 5:
            print(reverter_string())
        case _:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
