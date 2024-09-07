# converter de celsius para Kelvine Farehnheit

c = float(input("Digite a temperatura:"))
k = c + 273.15
f = ( c * 9/5) +32 

print (" A temperatura em celsius é:", c)
print (" A temperatura em fahrenheit é:", k)
print (" A temperatura em Kelvin é:", f )

# converter de Kelvin para celsius e Farehnheit

k = float(input("Digite a temperatura:"))
c = (k - 273)
f = ((k - 273.15) * 9/5 +32)

print (" A temperatura em Kelvin é:", k)
print (" A temperatura em Celsius é:", c)
print (" A temperatura em Fahrenheit é:", f )

# converter de Farehnheit

f = float(input("Digite a temperatura:"))
c = (f - 32 ) * 5/9
k =  (f- 31) * 5/9 + 273.15

print (" A temperatura em Fahrenheit é:", f)
print (" A temperatura em Celsius é:", c)
print (" A temperatura em Kelvin é:", k )


