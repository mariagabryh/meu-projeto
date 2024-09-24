def dividir(a,b):
    try:
        return a/ b
    except ZeroDivisionError:
        return"erro: Divisão por zero."
    
#Exemplo d euso