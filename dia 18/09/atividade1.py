# Declrando as listas
nomes = ["João", "Maria", "Pedro"]
idades = [30,25,50]

# Exibindo o conteudo das listas
print(nomes[0])
print(idades[0])

for i in range  (len(idades)):
    print(nomes[i])
    print(idades[i])

nomes.append("joana")
idades.append(41)

# Exibindo o todo conteudo das listas

for i in range  (len(idades)):
    print(f"Sr(a) {nomes[i]}, a sua idade é {idades[i]} anos. ")

for i in range  (len(idades)):

    nomes.append(input("Informe o nome: "))
    idades.append(int(input("Informe a idade: ")))
    
    for i in range  (len(idades)):
        print(nomes[i])
        print(idades[i])
