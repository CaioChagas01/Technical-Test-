from typing import Set, List

# A função abaixo irá:
# - Receber um conjunto A com até 4 elementos.
# - Converter o conjunto em uma lista para acesso por índice.
# - Calcular o número total de subconjuntos possíveis (2^n).
# - Utilizar um laço para gerar todas as combinações de elementos com base em bits.
# - Para cada combinação, criar um subconjunto correspondente.
# - Armazenar cada subconjunto como um frozenset (conjunto imutável) para poder ser inserido em outro set.
# - Retornar um conjunto contendo todos os subconjuntos de A.

def getSubSets(A: Set[int]) -> Set[frozenset]:
    lista = list(A)
    n = len(lista)
    resultado = set()

    # Total de subconjuntos: 2^n
    for i in range(2 ** n):
        subconjunto = set()
        for j in range(n):
            if (i >> j) & 1:
                subconjunto.add(lista[j])
        resultado.add(frozenset(subconjunto))  

    return resultado 



A = {1, 2, 3}
subconjuntos = getSubSets(A)
for s in subconjuntos:
    print(set(s))  # Exibe cada subconjunto de forma legível
