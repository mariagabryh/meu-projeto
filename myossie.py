# Declaração de variaveis...
empresa = input('Qual é a empresa?') 

rh = input("Quem é o gestor responsável")

cargo = input("DIgite o seu cargo atual na empresa")

inicio = input("Digite a data de inicio do aviso prévio")

termino = input("Digite a data de término do aviso prévio")

local = input("Digite o local e data")

assinatura = input("Faça a sua assinatura aqui")

nome = input("Digite o seu nome completo")

# Exibição

print("Á," ,{empresa})

print("Prezado(a)",{rh})

print("Venho por meio desta carta comunicar formalmente meu pedido de demissão do cargo de",  {cargo}, )

print("Estarei á disposição da empresa durante o aviso prévio, no período de", {inicio}, {termino})

print("Local:",{local})

print ("Assinatura:",{assinatura})

print("Nome completo:" ,{nome}, )