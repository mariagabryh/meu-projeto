#Pagamento
valor = float(input("Insira o valor do produto: "))
ot = int(input("Insira a quantidade de parcelas: "))
taxa = float(input("Insira a taxa de juros: "))
acumulado = 0

parcela = valor/ot
for x in range (0,ot):
    print(f"Deseja pagar a {x + 1} parcela? ")
    pagar = input()
    if pagar == 'sim':
        parcela = parcela * (1+taxa)
        acumulado = acumulado + parcela
        print(acumulado)
        continue
    else:
        break
    

