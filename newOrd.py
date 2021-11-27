import time
from typing import List
from implementacoes import desempenhoAlgoritmo


def bubbleSort(v: List[int]):

    t1 = time.perf_counter_ns()
    numComp = 0
    numOp = 0

    numOp += 2              # atribuicao i, n-1
    numComp += 1            # comaparacao inicial do for

    for i in range(0, len(v) - 1):

        numOp += 2          # atribuicao do j, n-i-1
        numComp += 1        # comparacao for
        for j in range(0, len(v) - (i+1)):

            numComp += 1    # if
            numOp += 1    # j+1

            if (v[j] > v[j+1]):

                aux = v[j]
                v[j] = v[j+1]
                v[j+1] = aux

                numOp += 5  # atribuicao, j+1, j+1

            numComp += 1    # comparacao for
            numOp += 1    # incremento j

        numComp += 1    # comparacao for
        numOp += 1    # incremento i
        print(v)

    t2 = time.perf_counter_ns()
    desempenhoBubble = desempenhoAlgoritmo((t2-t1)/1000000, numOp, numComp)
    return desempenhoBubble
