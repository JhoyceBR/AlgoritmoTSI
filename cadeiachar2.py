cadeia = input("digite um texto: ")
contador = 0
for i in range(0, len(cadeia)):
    if(cadeia[i] == 'o'):
        contador += 1
print("a letra o apareceu " + str(contador)+ " vez(es)")