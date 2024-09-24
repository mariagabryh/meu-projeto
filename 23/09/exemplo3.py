def comb(d,c):
    try:
        litros = d/c
    except ZeroDivisionError:
        print("Verifique o consumo informado.")
    print(f"A quantida de combustivel gasto foi {litros:.2f} litros.")
while True:
    try:
        distancia = float(input("Informe a distancia percorrida: "))
        consumo = float(input("Informe o consumo médio do veículo: "))
    except ValueError:
        print("Verifique os valores informados. ")
    else:
        comb(distancia,consumo)
        break