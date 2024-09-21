# Declaração de variaveis
resp = 'S'
sexo = []
olhos = []
cabelos = []
idade = []
qtd_sexo_f = 0 
qtd_olhos_cabelos = 0
# Iniciando o bloco de repetição

while resp == 'S' or resp == 's':

# Coletando as informações
    
    idade.append(int(input("Informe a idade: ")))
    sexo.append(input("Informe o Sexo - (M)Masculino ou (F)Feminino : "))
    olhos.append(input("Informe a cor dos olhos - (A)Azuis ou (V)Verdes ou (C)Castanhos : "))
    cabelos.append(input("Informe a cor dos cabelos - (L)Louro ou (C)Castanhos ou (P)Pretos : "))
    resp = input("Deseja continuar(S/N)? ")

# Finalizando o bloco de retição
    
maior_idade = max(idade)

for i in range(len(idade)):
    if(sexo[i] == "F" or sexo[i] =='f') and (idade[i] >= 18 and idade[i] <= 35):
        qtd_sexo_f += 1
    if(olhos[i] == "V" or sexo[i] =='v') and (cabelos[i] == 'L ' or cabelos[i] == 'l'):
        qtd_olhos_cabelos += 1
# Exibições
print(f"A maior encontrada foi {maior_idade} anos.")
print(f"A quantidade de pesoas do sexo feminino com idade entre 18 e 35 foi {qtd_sexo_f}")
print(f"A quantidade de pessoas com cabelos louros e olhos verdes foi {qtd_olhos_cabelos} ")