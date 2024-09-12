# Demonstração de operadores lógicos em condicionais

print("O que voce vai fazer amanhã de manha?")
print("dormir / estudar / planejar")
MANHA = input()
print("O que voce vai fazer amanhã de tarde")
print("jogar / treinar / trabalhar")
TARDE = input()

if not MANHA or not TARDE :
    print("Voce precisa dizer o que vai fazer!")
else: 
    if MANHA == "dormir" or TARDE == 'jogar':
        print("Voce está desperdiçando o seu dia!")
    elif MANHA == 'estudar' or TARDE == 'treinar':
        print("Que bom voce ira de aperfeiçar!")
    elif MANHA == "planejar" and TARDE == "trabalhar":
        print ("Para trabalhar melhor, devo planejar!")
    else: 
        print("Não combinamos estas ações...")

print('Tenha um bom dia!')