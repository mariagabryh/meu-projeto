def calcular(n1,n2,op):
    def so(num1,num2):
        return num1 + num2
    def sub(num1,num2):
        return num1 - num2
    def multip(num1,num2):
        return num1 * num2
    def div(num1,num2):
        return num1 / num2
    if op == "+":
        result = so(n1,n2)
    if op == "-":
        result = sub(n1,n2)
    if op == "*":
        result = multip(n1,n2)
    if op == "/":
        result = div(n1,n2)
    else:
        print("Operador matematico invalido.")
    return result
n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
op = input("Informe o operador matematico(soma (+), subtração(-), multiplicar (*) ou divisão(/)): ")
print(calcular(n1,n2,op))