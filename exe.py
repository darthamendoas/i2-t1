aluno=""
total=0
mediag=0
soma=0
while aluno != "fim":
    aluno=input("Digite o nome do aluno (ou 'fim' para sair): ")
    if aluno=="fim":
        break
    n1=float(input("Qual é a nota 1: "))
    if n1>10 or n1<0:
        print("Nota invalida.")
        continue
    n2=float(input("Qual é a nota 2: "))
    if n2>10 or n2<0:
        print("Nota invalida.")
        continue
    media=(n1+n2)/2
    print("A média do aluno é:",media)
    total+=1
    soma+=media
mediag=soma/total
print("--- Relatório Final ---")
print("Total de alunos:",total)
print("Média geral da turma:",mediag)