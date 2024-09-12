# Eclipse

LOCAL = input("Digite o estado:(RJ/SP/MG/ES) ")
print("Esteve no horario exato do eclipse?")
HORA = int(input("Se sim, digite 0; se não, digite os minutos: "))
DIA = input("O dia está claro? (S/N)")

if DIA == "S":
    if LOCAL == "RJ" and HORA == 0:
        print("Eclipse total!")
    elif (LOCAL == "RJ" or LOCAL == "SP" or LOCAL == "MG " or LOCAL == "ES") and (HORA >= -5 and HORA <= 5):
        print("Eclipse Parcial!")

    else:
        print('Não estava no lugar e na hora certa!')
else:
    print("Tempo ruim para assistir...")