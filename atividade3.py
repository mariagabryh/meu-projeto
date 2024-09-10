# Atividade 3
peso = float(input("Digite seu peso:"))
altura = float (input("Digite sua altura:"))

imc = (peso / altura * altura )

if imc < 18:
    print("Abaixo do peso ideal")
elif imc > 25:
    print("Acima do peso ideal")
else:
    print("Seu peso está OK")