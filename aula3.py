a = int(input('Primeiro bimestre: '))
if a>10:
    a = int(input('Voce digitou errado. \nPrimeiro bimestre: '))
b = int(input('Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
media = (a + b + c + d)/4
if a<= 10 and b<=10 and c<=10 and d<=10:
    print('Media: {}'.format(media))
else:
    print('Foi informado alguma nota errada')

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um número é par')
# else:
#     print('Nenhum número par foi digitado')
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('terceiro valor: '))
#
# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior número é {}'.format(b))
# else:
#     print('o maior número é {}'.format(c))
# print('final do programa')
