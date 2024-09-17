# Declaração de variaveis 
resp = 'S'
acumulador = 0
etanol = 3.70
gasolina_comum = 5.39
gasolina_aditivada = 5.75
diesel = 4.90
acumulador2 = 0


# Inicio do programa

while resp == 'S' or resp == 's':
    ETANOL = int(input("Quantos litros de etanol foi vendido? "))
    COMUM = int(input("Quantos litros de gasolina comum foi vendido? "))
    ADITIVADA = int(input("Quantos litros de gasolina aditivada foi vendido? "))
    DIESEL = int(input("Quantos litros de Diesel foi vendido? "))
    acumulador = acumulador + ETANOL + COMUM + ADITIVADA + DIESEL

    resp = input(f"Deseja continuar? (S/N): ")
 
# Exibidor de resultados
    print(f"Foram vendidos {acumulador} litros de combustíveis hoje. ")
    print(f"Foram vendidos R${ETANOL*etanol:.2f} de Etanol hoje. ")
    print(f"Foram vendidos R${COMUM*gasolina_comum:.2f} de gasolina comum hoje. ")
    print(f"Foram vendidos R${ADITIVADA*gasolina_aditivada:.2f}  de Gasolina Aditivada hoje. ")
    print(f"Foram vendidos R${DIESEL*diesel:.2f} de Diesel hoje. ")



