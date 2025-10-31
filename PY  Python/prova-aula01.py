alunos = []
for i in range(5):
    nome = input(f'Digite o nome do aluno: ')
    nota = float(input(f'Digite a nota do aluno: '))
    alunos.append((nome, nota))

maior_nota = 0
nome_maior_nota = ""
for aluno in alunos:
    nome, nota = aluno
    if nota > maior_nota:
        maior_nota = nota
        nome_maior_nota = nome

print(f'O aluno com a maior nota é {nome_maior_nota} com a nota {maior_nota}')
