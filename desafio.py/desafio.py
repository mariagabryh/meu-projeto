# Variaveis
idade = []
sexo = []
resp = 0
resp2 = []
qnd_sim = 0
qnd_nao = 0
qnd_menor18 = 0
qnd_maior18 = 0
sexo_feminino_maior = 0
sexo_masculino_menor = 0
# Insersão de dados
while resp == "S" or resp == 's':
    idade.append = (int(input("Insira a sua idade: ")))
    sexo.append = input("Insira seu sexo (M - Masculino ou F - Feminino): ")
    resp2 = input("Voce gostou do produto? (S/N): ")
    resp = input("Deseja continuar? (S/N)")
for i in range(len(idade,sexo,resp2)):
    if resp == "S" or "s":
        qnd_sim += 1
    if resp == "N" or "n":
        qnd_nao += 1
    if idade[i] <= 18 :
        qnd_maior18 += 1
    if idade[i] >= 18 :
        qnd_menor18 += 1






#Exibições
