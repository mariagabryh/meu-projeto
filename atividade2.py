# Atividade 2
print("Digite a sua nota em portugues:")
nota = float(input())
print("Digite a sua nota em matematica:")
nota2 = float(input())
print("Digite a sua nota em ciencias:")
nota3 = float(input())
print("Digite a sua nota em geografia:")
nota4 = float(input())

soma = (nota + nota2 + nota3 + nota4 /3)

if soma >= 6 :
    print("Aluno aprovado")
else:
    print("Aluno reprovado")