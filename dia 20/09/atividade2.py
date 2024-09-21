# Declração de variaveis
alunos = ["Ana","Rebeca,Gustavo","Luisa","Rodrigo",'Maria,Luis',"Marcelo","Beatriz","Julia"]
notas = [7.5,8,5,7.5,10,4.5,8.5,6.5,3,9.5]
qnt_maior = 0
qnt_menor = 0
# Descobrindo a maior nota
maior_nota = max(notas)
posicao = alunos.index(maior_nota)
melhor_aluno = alunos[posicao]
# Calculo das médias
media = sum(notas) / len(notas)
for i in range(len(notas)):
    if notas [i] > media:
        qnt_maior += 1
    elif notas [i] < media:
        qnt_menor += 1 
# Exibição
print(f"A média é:{media:.2}")
print("A quantidade de alunos acima da média é: ", qnt_maior)
print("A quantidade de alunos abaixo da média é: ", qnt_menor)
print(f"O aluno com a melhor nota é {melhor_aluno} e sua nota foi {maior_nota}")








