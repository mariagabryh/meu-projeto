# Tabela 

time = input("Digite o seu time: ")
posiçao = int(input("Qual posição? "))

if posiçao == 1:
    print("Campeão!")

elif posiçao >= 1 and posiçao <= 6:
    print("Libertadores!")

elif posiçao >= 7 and posiçao <= 12 :
    print("Sul-Americana!")

elif posiçao == 'entre os 4 ultimos' :
    print("Rebaixado")

elif posiçao  >= 13 and posiçao <= 17:
    print("Sem Classificação.")

elif posiçao >= 18 and posiçao <= 20 :
    print("Rebaixado!")


else:
    print("Valor incorreto!...")




