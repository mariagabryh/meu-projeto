#Futebol

FUNÇAO = input("Digite a função que voce pode exercer em um jogo:")

if FUNÇAO == 'goleiro' or FUNÇAO ==  'zagueiro' or FUNÇAO == 'lateral':
    print("Defesa!")
elif FUNÇAO == 'ala' or FUNÇAO == 'volante' and FUNÇAO ==  'meia':
        print("Meio-Campo!")
elif FUNÇAO == 'ponta' or FUNÇAO == 'atacante' and FUNÇAO ==  'centroavante':
            print("Ataque!")
            
else:
    print("Teimoso!")
