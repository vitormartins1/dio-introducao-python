for num in range(101):
    div = 0
    for x in range(1, num):
        resto = num % x
        print(x, resto)
        if resto == 0:
            div += 1

    if div == 2:
        print('número {} é primo'.format(num))
    else:
        print('número {} não é primo'.format(num))

# a = int(input('Entre com um numero: '))
# div = 0
#
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))