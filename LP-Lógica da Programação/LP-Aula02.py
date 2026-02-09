horas = int(input('digite quantas horas você trabalhou: '))
valor_hora_normal= int(input('digite o valor da hora normal: '))
if horas > 44:
    horas_extras = horas - 44
    valor_hora_extra = valor_hora_normal * 1.5
    receber= (horas * valor_hora_normal)+(horas_extras * valor_hora_extra)
    print(f'{horas_extras} Horas extras a R${valor_hora_extra} cada')

else: 
    receber= horas * valor_hora_normal
    print(f'Jornada foi cumprida corretamente.')
