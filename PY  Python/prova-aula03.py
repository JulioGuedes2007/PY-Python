alunos = {} 
num_alunos = int(input("Quantos alunos deseja cadastrar? "))
for i in range(num_alunos):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(1,4):
        nota = float(input(f"Digite a nota {i} de {nome}: ")) 
        notas.append(nota)
    alunos[nome] = notas
aprovados = []
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    if media >= 7:
        aprovados.append((nome, media))
print("Alunos aprovados:")
for nome, media in aprovados:
    print(f"{nome}: {media:.2f}")
