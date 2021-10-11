conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print('Uniao: {}'.format(conjunto_uniao))

conjunto_intersecao = conjunto.intersection(conjunto2)
print('intersecao: {}'.format(conjunto_intersecao))
conjunto_diferença1 = conjunto.difference(conjunto2)
conjunto_diferença2 = conjunto2.difference(conjunto)
print('diferenca entre 1 e 2: {}'.format(conjunto_diferença1))
print('difernca entre 2 e 1: {}'.format(conjunto_diferença2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('diferenca simetrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um subconjunto de A: {}'.format(conjunto_superset))

lista = {'cachorro', 'cachorro', 'gato', 'gato', 'elefante'}
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

# conjunto = {1,2,3,4,4,2}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)