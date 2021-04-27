lista = [1, 2, 3, 4, 5, 0]

def quicksort(lista, l, h): # apontadores low = baixo high= alto
    if(h>l): # tem pelo menos 2 elementos
        ip = particao(lista, l, h) # indice do pivor, onde os elementos a esquerda do indice são menores e da direita são mairoes
        quicksort(lista, l, ip-1) # chamada para a partição a esquerda do pivo
        quicksort(lista, ip+1, h)

def particao(lista, l, h):
    pivo = h # indice do ultimo elemento
    pa = l # primeiro da esquerda
    for i in range(l, h):  
        if lista[i]<lista[pivo]:
            lista[i], lista[pa] = lista[pa], lista[i]
            pa += 1
    lista[pivo], lista[pa] = lista[pa], lista[pivo]
    return pa
    
