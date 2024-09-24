
def  soma(x,y):
    result = x +y
    print(f"O resultado da soma é {result}")
    try:
        n1 = int(input("Informe um valor inteiro: "))
        n2 = int(input("Informe um valor inteiro: "))
    except ValueError:
        print("Verifique os valores fornecidos ")
    else:
        soma(n1,n2)




