from os import error
import time
from typing import List
import random


class desempenhoAlgoritmo():
    def __init__(self, tempo, numOp, numComp) -> None:
        self.tempo = tempo
        self.numOp = numOp
        self.numComp = numComp

    def to_string(self):
        print("Tempo de execução: {:5}".format(str(self.tempo)) + " ms")
        print("Numero de Operações: " + str(self.numOp))
        print("Numero de Comparações: " + str(self.numComp))


def vectorGeneretor(tipoVetor, tamanho):
    vetor = []
    for _ in range(tamanho):
        vetor.append(random.randint(0, 100))
    if tipoVetor == 1:
        return vetor
    elif tipoVetor == 2:
        vetor.sort()
        return vetor
    elif tipoVetor == 3:
        vetor.sort(reverse=True)
        return vetor


def insertionSort(v: List[int]):

    t1 = time.perf_counter_ns()
    numComp = 0
    numOp = 0

    numComp += 1            # entrar no for
    numOp += 1              # atribuicao i

    for i in range(1, len(v)):

        elemento = v[i]
        j = i - 1

        numOp += 3          # atribuicao, atribuicao, i-1

        numOp += 1          # and do while
        numComp += 2        # entrar no while

        while (j >= 0 and v[j] > elemento):

            v[j+1] = v[j]
            j = j - 1

            numOp += 5      # atribuicao, j+1, atribuicao, j-1, and do while
            numComp += 2    # condicao while

        v[j+1] = elemento

        numOp += 3          # j+1, atribuicao, incrementar i
        numComp += 2        # condicao while
        print(v)
    t2 = time.perf_counter_ns()
    desempenhoInsertion = desempenhoAlgoritmo((t2-t1)/1000000, numOp, numComp)
    return desempenhoInsertion


def selectionSort(v: List[int]):

    t1 = time.perf_counter_ns()
    numComp = 0
    numOp = 0

    numComp += 1            # entrar no for
    numOp += 1              # atribuicao i

    for i in range(1, len(v)):

        elemento = v[i]
        j = i - 1

        numOp += 3          # atribuicao, atribuicao, i-1

        numOp += 1          # and do while
        numComp += 2        # para entrar no while

        while (j >= 0 and v[j] > elemento):

            v[j+1] = v[j]
            j = j-1

            numOp += 5      # atribuicao, j+1, atribuicao, j-1, and do while
            numComp += 2    # condicao while

        v[j+1] = elemento

        numOp += 3          # j+1, atribuicao, incrementar i
        numComp += 1        # condicao for

        print(v)
    t2 = time.perf_counter_ns()
    desempenhoSelection = desempenhoAlgoritmo((t2-t1)/1000000, numOp, numComp)
    return desempenhoSelection
