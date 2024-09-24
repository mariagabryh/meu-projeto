
def transformar_unidades(numero,unidade):



    while True:
        if unidade != '':
            break

        if unidade == "cm" or unidade == 'CM':
            print(f"{numero} cm é igual a {numero/100:.2f}m.")
            break
        else:
            print("Verfique o nome digitado.")
    while True:
elif unidade == "m" or unidade == 'M':
print(f"numero m é igual a {numero * 100:.2f}cm.")
else:
print("Unidade invalida use m ou cm. ")
    
    #Exibição
numero = float(input("Insira o valor a ser calculado: "))
unidade = input("Unidade (CM/M).")

transformar_unidades(numero,unidade)