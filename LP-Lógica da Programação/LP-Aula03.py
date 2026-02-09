salario_normal=float(input('Digite seu salario normal: '))
tempo_trabalhado= int(input('Digite quantos meses você trabalhou: '))

if tempo_trabalhado<12:
    salario_ferias=salario_normal * (1/12*tempo_trabalhado)
    print('ferias proporcionais de R$', salario_ferias)

elif tempo_trabalhado==12:
    print('você trabalhou o ano todo')

else:
    print('não é possível trabalhar mais de 12 meses em um ano')
