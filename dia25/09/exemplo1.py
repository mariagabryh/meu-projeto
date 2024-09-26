def calcular(num,unidade):
    def m(n):
        return n/100
    def cm(n):
        return n*100
    if unidade == 'm':
        result = "{} centimetros." .format(cm(num))
    elif unidade == "cm":
        result= "{} metro." .format(m(num))
    else:
        result = "Verifique a unidade de medida."
    return result
while True:
    try:
        n = int(input("Informe o valor da medida: "))
        u = input("Informe a unidade de medida(cm ou m)")
    except ValueError:
        print("Verifique a entrada de dados")
    else:
        print(calcular(n,u))
        break

