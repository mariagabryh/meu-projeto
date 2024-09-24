# Variaveistry:
def calcular_pagamento():
    try:
        nome = input("Digite o sue nome: ")
        horas_extras = int(input("Digite as horas extras trabalhadas: "))
        if horas_extras == 0:
            raise ZeroDivisionError
        pagamento = horas_extras * 50
        print(f"Sr(a) {nome}, Voce ira receber R${pagamento} por suas horas extras trabalhadas.")
    except ValueError:
        print("Insira um número válido.")
    except ZeroDivisionError:
        print("Não foi possivel realizar o resultado.")
calcular_pagamento


