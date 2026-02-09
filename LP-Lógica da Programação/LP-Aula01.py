tempo_servico = float(input('digite o seu tempo de serviço em meses: '))
valor_fgts = float(input('digite o valor do seu fgts: '))
valor_fgts = float(input('digite o saldo do seu fgts: '))

if tempo_servico > 12:
    valor_a_pagar= 0.4*valor_fgts
