# Variaveis
def calcular(n1,n2,op):
    def so(num1,num2):
        return num1 + num2
    def sub(num1,num2):
        return num1 - num2
    def div(num1,num2):
        return num1/num2
    def mult(num1,num2):
        return num1 * num2
    if op == "so":
        result = "a soma é:{}" .format(so(n1,n2))
    if op == "sub":
        result = "a subtração é:{}" .format(sub(n1,n2))
    if op == "div":
        result = "a divisão é:{}" .format(div(n1,n2))
    if op == "m":
        result = "a  multiplicação é:{}" .format(mult(n1,n2))
    else:
        print("Operador matematico invalido.")
    return result

n1 = int(input("informe um número: "))
n2 = input("Informe um número: ")
op = input("informe o operador matematico : so - Soma, sub - Subtração, div - Divisão ou m - Multiplicação.")
print(calcular(n1,n2,op))
