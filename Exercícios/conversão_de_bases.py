num = int(input('digite um numero inteiro: '))
opção = int(input('''escolha um metodo de conversão:
[1] binario
[2] octal
[3] hexadecimal '''))
if opção== 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(opção)[2:]))
elif opção== 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(opção)[2:]))
elif opção== 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(opção)[2:]))
else:
    print('opção invalida! tente novamente...')