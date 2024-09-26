
def transformar_unidades(numero,unidade):
    media_cm = numero/100
    media_m = numero * 100
    while True:
        if unidade != '':
            break

        if unidade == "cm" or unidade == 'CM':
            print(f"{numero} cm é igual a {media_cm:.2f}m.")
            break
        else:
            print("Verfique o nome digitado.")
    
            
elif unidade == "m" or unidade == 'M':
print(f"numero m é igual a {media_m:.2f}cm.")
else:
print("Unidade invalida use m ou cm. ")
    
    #Exibição
numero = float(input("Insira o valor a ser calculado: "))
unidade = input("Unidade (CM/M).")

transformar_unidades(numero,unidade)