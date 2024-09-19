numero = [30,25,50,10,15,25,40,90,85,20]
par=0
impar = 0
for i in range(len(numero)):
    if numero[i] & 2 == 0: #%para calcular o resto da divisão
        par += 1
    else:
        impar +=1

print("A quantidade de numeros pares é ", par)
print("A quantidade de numeros impares é ", impar)

