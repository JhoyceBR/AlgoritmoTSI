lista = [1,2,3,4,5,6,7,8]
def binariarecursiva(lista, inferior, superior, key):
    if superior<inferior:
        return -1
    
    meio = (inferior+superior)//2

    if(lista[meio]==key):
        return meio
    elif(lista[meio]>key):
        return binariarecursiva(lista, inferior, meio-1, key)
    else:
        return binariarecursiva(lista, meio+1, superior, key)
    
print(binariarecursiva(lista, 0, 7, 40)) # teste do pior caso