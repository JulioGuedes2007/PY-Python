salario = float(input('Digite seu salario: '))
dias_atraso = int(input('Digite quantos dias de atraso a empresa teve: '))

if dias_atraso > 5:
    for i in range(1, dias_atraso + 1):
        salario += salario * 0.01
    print(f'Seu salario com multa é de: R$ {salario:.2f}')
else:
    print('Não houve multa no salario')
