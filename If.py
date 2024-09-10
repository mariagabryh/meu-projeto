# Demonstração do uso de if/elif/else...
print("Digite sua idade:")
Age = int(input())

if Age < 18:
    print("Voce não é maior de idade!")
    print("Não podera realizara a operação!")
elif Age >= 65:
    print("Voce já está pronto para se aposentar?")
    print("Poderemos oferecer suporte técnico...")
else: 
    print("Voce é maior de idade.")
    print("Portanto, poderá realizar a operação.")
print("Obriado por optar pelos nossos serviços!")

