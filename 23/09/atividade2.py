def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print('Verifique o denominador')
    else:
        print(f"O resultado é: {result}")
try:
    n1 = int(input("Insira um numerador: "))
    n2 = int(input("Insira o denominador: "))
except ValueError:
    print("Verifique a entrada de dados. ")
else:
    divide(n1,n2)