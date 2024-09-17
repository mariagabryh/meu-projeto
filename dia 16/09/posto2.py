# Declaração de variaveis 
resp = 'S'
etanol = 3.70
gasolina_comum = 5.39
gasolina_aditivada = 5.75
diesel = 4.90
qnd_e = 0
qnd_cg = 0
qnd_ga = 0
qnd_d = 0


# Inicio do programa

while resp == 'S' or resp == 's':
    GASOLINA = input("Digite o tipo de combustivel:E - etanol, GC - Gasolina Comum, GA - Gasolina Aditivada, D - Diesel. ")
    LITROS = float(input("Digite a quantidade de litros: "))
# Calculando
if GASOLINA == 'E' or "e":
    qnd_e = qnd_e + GASOLINA
if GASOLINA == 'CG' or "cg":
    qnd_cg = qnd_cg + GASOLINA
if GASOLINA == 'GA' or "ga":
    qnd_ga = qnd_ga + GASOLINA
if GASOLINA == 'D' or "d":
    qnd_d = qnd_d + GASOLINA
else:
    print("Este tipo de combustivel não existe! ")
    resp = input("Deseja continuar (S/N)? ")
# Apresentando Resultados
print(f"A quantidade total de litros vendido foi de {qnd_e} litros, gerando um montante de R${(qnd_e * etanol):.2f}")
print(f"A quantidade total de litros vendido foi de {qnd_cg} litros, gerando um montante de R${(qnd_cg * gasolina_comum):.2f}")
print(f"A quantidade total de litros vendido foi de {qnd_ga} litros, gerando um montante de R${(qnd_ga * gasolina_aditivada):.2f}")
print(f"A quantidade total de litros vendido foi de {qnd_d} litros, gerando um montante de R${(qnd_d * diesel):.2f}")
