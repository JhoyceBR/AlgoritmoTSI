#var=input("digite um numero ai nego: ")
#var = int(var)
#var = var+1
#print(var)

#a, b = input("digite dois numeros ai nego: ").split()
#c = float(a)+float(b)
#print(c)

#a = 1
#b = 2
#c = a+b
#print("A soma " +str(c) + "!!!")

#import math
#print("o valor de pi é: " +str(math.pi))

#import math
#print(f'o valor de pi formatado é:{math.pi:20.4f}')

#year = 2020
#mes = 'referendo'
#print(f'resultado do {mes} de {year}')

#votos_sim = 42572654 
#votos_nao = 43132495
#percentual = 100*votos_sim/(votos_sim+votos_nao)
#texto = 'percentual {:20} de votos SIM {:20.2f}'.format(votos_sim, percentual)
#print(texto)

#print('{0} e  {1}'.format('ovo', 'cuscuz'))
#print('{1} e  {0}'.format('ovo', 'cuscuz'))

#print('Esta {food} está {gosto}'.format(food="comida", gosto="boa"))

#import math
#print('o primeiro numero vale {numero1:.2f}; pi val {numero2:4.2f}.'.format(numero1=0.123, #numero2=math.pi))

# Operadores aritmétricos

# +
# -
# *
# /- divisão real
# // - divisão inteira
# % - resto da divisão inteira
# ** x**y

#a, b, c = input("digita aí nego 3 valor: ")
#a = float(a)
#b = float(b)
#c = float(c)
#delta = b**2-4*a*c
#print(delta)

# Operadores lógicos

# and = e
# or = ou
# not = ! 

# Operadores relacionais
# compara valores, o resultado pode ser true ou false

# == igual	
# > maior	
# >= maior ou igual	
# < menor
# <= menor ou igual
# != difente

# Escreva um programa que diz se uma equação do segundo grau tem duas raízes, uma ou nenhuma raíz real

a , b, c = input("diga os coeficientes ai homi: ").split()
a = float(a)
b = float(b)
c = float(c)
delta = b**2-4*a*c
duasr = delta>0
umar = delta== 0
semr = delta<0

#print("possui duas raizes é: "+str(duasr))
#print("possui uma raíz é: "+str(umar))
#print("possui nenhuma raíz é: "+str(semr))

if(delta>0):
	print("Possui duas raízes")
elif(delta==0):
	print("Possui uma raíz")
else:
	print("Não possui raízes")


