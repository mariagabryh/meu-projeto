# Conversão de temperatura
print("Escolha entre celsius, fahrenheit e Kelvin")
print("C - celsius")
print("F - fahrenheit")
print("K -Kelvin ")

escala = input("Digite a sua escala escolhida: ")
temperatura = float(input("Digite a temperatura: "))
if  escala == 'C':

    k = temperatura + 273.15
    f = ( temperatura * 9/5) +32 

    print (" A temperatura em celsius é:", temperatura)
    print (" A temperatura em fahrenheit é:", k)
    print (" A temperatura em Kelvin é:", f )

# converter de Kelvin para celsius e Farehnheit
if escala == 'F':

    c = (temperatura - 273)
    f = ((temperatura - 273.15) * 9/5 +32)

    print (" A temperatura em Kelvin é:", temperatura)
    print (" A temperatura em Celsius é:", c)
    print (" A temperatura em Fahrenheit é:", f )

# converter de Farehnheit
if escala == 'K':

    c = (temperatura - 32 ) * 5/9
    k =  (temperatura - 31) * 5/9 + 273.15

    print (" A temperatura em Fahrenheit é:", temperatura)
    print (" A temperatura em Celsius é:", c)
    print (" A temperatura em Kelvin é:", k )


