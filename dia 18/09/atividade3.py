#Variveis
notas = []
resp = 'S'
soma_notas = 0
#Iniciando o bloco de reptiçao

while resp == 'S' or resp == "s":
    # Alimentando a lista

    notas.append(float(input("Informe as Notas: ")))
    resp = input("Deseja continuar? (S/N)")
# Finalizando o bloco de reptição
# Iniciando o bloco de repetição
    
for i in range(len(notas)):

    print(notas[i])#Exibindo o conteúdo da lista
    soma_notas = sum(notas)
# Finalizando o bloco de retição 
    
    print(" A média foi ", soma_notas/len(notas) )



