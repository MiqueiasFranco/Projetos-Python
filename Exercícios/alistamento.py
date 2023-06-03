from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print(' voce deve se alistar imediatamente!!')
elif idade < 18:
    saldo = 18 - idade
    ano = saldo + atual
    print('voce ainda possui {} anos e só precisara se alistar em {}'.format(idade, ano))
elif idade > 18:
    saldo =  idade - 18
    ano = atual - saldo
    print('voce deveria ter se alistado em {}'.format(ano))