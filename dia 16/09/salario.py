# Declaração de variaveis

soma_renda = 0
soma_filhos = 0
maior_renda = 0
qnt_renda = 0
cont = 0
resp = 'S'
# Inicio do código

while resp == 'S' or resp == 's':
    RENDA = float(input("Qual sua renda familiar? "))
    FILHOS = int(input("Quantos filhos tem? "))
    soma_renda = soma_renda + RENDA
    soma_filhos = soma_filhos + FILHOS
    # Coletando a Maior renda

    if RENDA > maior_renda:
        maior_renda = RENDA
 # Coletando a quantidade pessoa com menor rende que 1.500
        
    if RENDA < 1500:
        qnt_renda += 1
    # Acumulando a quantidade de pessoas
    cont +=1
    resp = input("Deseja continuar (S/N)? ")
3 # final do bloco de reptição
# Exibindo resultados

print(f"A Média das rendas é {soma_renda/cont}")
print(f"A média da quantidade de filhos é {soma_filhos/cont}")
print(f"A maior das rendas é R${maior_renda:.2f}")
print(f"O percentual de pessoas com o salario abaixo de R$ 1,500 é de {(qnt_renda/cont)*100}")