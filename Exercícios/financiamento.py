while True:
    salario = float(input('renda mensal: '))
    imovel = float(input('valor do imovel: '))
    tempo = int(input('digite o periodo do financiamento (anos): '))
    caltemp = tempo * 12
    calpor = salario * 30 / 100
    calparc = imovel / caltemp
    if calparc > calpor:
        print('sinto muito...voce não foi aprovado!')
    elif calparc < calpor:
        print(' parabens...seu financiamento foi aprovado com parcelas de {:.2f}'.format(
            calparc))
    opção = input('deseja continuar? [S/N] ')
    if opção == 'n':
        break
else:
    print('opção invalida! tente novamente...')
