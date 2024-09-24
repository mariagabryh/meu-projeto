n1 =0
n2 = 0
divisao = 0
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
divisao = n1 / n2
print(divisao)

def  divisão(n1,n2):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print("Verifique os valores fornecidos ")
