# Demonstração do uso de estrutura repetitiva
CONTADOR = 0; SENHA = ""
while SENHA != "S3nha":
    print("Digite a senha:")
    SENHA = input()

    if SENHA == "S3nha":
        print("Senha correta!")
        break
    else:
        print("Senha errada...")

    CONTADOR = CONTADOR +1
    if CONTADOR == 3:
        print("Tentativas excedidas!")
        break

   