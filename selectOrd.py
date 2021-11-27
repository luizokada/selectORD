from typing import Final
from implementacoes import selectionSort, insertionSort, vectorGeneretor
from newOrd import bubbleSort

funcoes: Final = {
    'selectionSort': selectionSort,
    'insertionSort': insertionSort,
    'bubbleSort': bubbleSort,

}


def getTamanho():
    while True:
        tamanho = input("Digite tamanho: ")
        try:
            val = int(tamanho)
            if val >= 0:
                break
            else:
                print("O tamanho não pode ser negativo")
        except ValueError:
            print("Tamanho precisa ser um inteiro")
    return val


def getTipoVetor():
    while True:
        tipo = input("Digite o tipo: ")
        try:
            val = int(tipo)
            if val > 0 and val <= 4:
                break
            else:
                print("O tipo é invalido")
        except ValueError:
            print("Tipo precisa ser um inteiro")
    return val


def getTipoOrd(numOrds):
    while True:
        tipo = input("Digite o tipo: ")
        try:
            val = int(tipo)
            if val >= 0 and val < numOrds:
                break
            else:
                print("O tipo é invalido")
        except ValueError:
            print("Tipo precisa ser um inteiro")
    return val


def printMenuVetor():
    print("Digite a forma que gostaria que o vetor inicial seja produzido")
    print("1- Sem nenhuma ordem especifica")
    print("2- Ordenado de forma crescente")
    print("3- Ordenado de forma Decrescente")
    print("4- Ordem inversa")
    print("ctrl + c para sair")


def printMenuOrd():
    index = 0
    keyVector = []

    for key in funcoes.keys():
        menssagem = str(index) + '- ' + str(key)
        print(menssagem)
        keyVector.append(key)
        index += 1
    return keyVector


def main():
    while True:
        try:
            printMenuVetor()
            tipoVetor = getTipoVetor()
            tamanho = getTamanho()

            keyVector = printMenuOrd()

            tipoOrd = getTipoOrd(len(keyVector))
            vetor = vectorGeneretor(tipoVetor, tamanho)

            des = funcoes[str(keyVector[int(tipoOrd)])](vetor)
            des.to_string()
            print(vetor)
        except KeyboardInterrupt:
            exit()


if __name__ == "__main__":
    main()
