lista = [12,10,7,5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
# print(lista_animal[1])
# novalista = lista_animal * 3
#
# print(novalista)

lista.sort()
lista_animal.sort()
# print(lista)
# print(lista_animal)

tupla = (1,10,12,14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(lista_numerica)

# soma = 0
#
# if ('lobo' in lista_animal):
#     print('existe um lobo na lista')
# else:
#     print('nao existe um lobo na lista. Será incluido.')
#     lista_animal.append('lobo')
#     print(lista_animal)
#
# # lista_animal.pop(1)
# # print(lista_animal)
#
# lista_animal.remove('elefante')
# print(lista_animal)