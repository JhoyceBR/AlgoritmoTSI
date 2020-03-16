nome = input("Digite seu nome: ")
nome2 = ""
for t in nome.split():
    t = t.lower()
    a=t[0].upper()
    nome2 = nome2+t+" "
nome2 = a + nome2[1:len(nome2)-1]
print(nome2)