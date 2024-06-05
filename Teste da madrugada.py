notas = []

for i in range(2):
    codigo_aluno = input('insira o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))

    resultado = [codigo_aluno, nota]

    notas.append(resultado)

for n in notas:
    codigo_aluno = n[0]
    notas = n[1]
    print(f'O aluno: {codigo_aluno}, tirou a nota {notas}')
    print(notas)