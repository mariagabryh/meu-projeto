# Atividade 1
print("Digite o dia da semana: ")
print("1.segunda-feira: Ir a academia. ")
print("2. terça-feira: Ver um filme no cinema.")
print("3. quarta-feira: Ir a praia.")
print("4. quinta-feira: Ler um livro")
print("5. sexta-feira: Ir a um restaurante.")
print("6. Sábado: Ir a uma festa")
print("7. Doming: Descansar e fazer um spay day")
DAY = int(input())
match DAY:
    case 1:
        print("Voce ira na segunda. Ótimo!")
    case 2:
        print("Voce ira na terça. Ótimo!")
    case 4:
        print("Voce ira na quarta. Ótimo!")
    case 4:
        print("Voce ira na quinta. Ótimo!")
    case 5:
        print("Voce ira na sexta. Ótimo!")
    case 6:
        print("Voce ira no sábado. Ótimo!")
    case 7:
        print("Voce ira no domingo. Ótimo!")
    case _:
        print("Opção não reconhecida!")
