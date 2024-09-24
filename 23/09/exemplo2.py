# Criando a função cálculo
valor = 50
def calculo(valor):
    result = valor * 50
    print(f"Sr(a) {nome}, voce ira receber o valor de R$ {result} por suas horas extras trabalhdas.")
while True: #Inciando o loop infinito
    nome = input("Informe o nome do funcionário: ")
    if nome != '':
            break #Finalizando o loop infinito
    else:
            print("Verfique o nome digitado.")
while True: #Iniciando outro loop infinito
    try:
        horas_extras = float(input("Informe a quantidade de horas trabalhadas: "))
    except ValueError:
        print('Verifique a quantidade de horas extras.  ')
    else:
        calculo(horas_extras)
        break #Finalizando o loop infinito
    