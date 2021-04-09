# Algoritmo de ordenação por Selection. 

lista = [7, 5, 1, 8, 3]

def selectionSort(lista):
    tamanho = len(lista)

    for j in range(tamanho-1):
        IndexMinimo = j

        for i in range(j, tamanho):
            if lista[i] < lista[IndexMinimo]:
                IndexMinimo = i

        if lista[j] > lista[IndexMinimo]:
            lista[j], lista[IndexMinimo] = lista[IndexMinimo], lista[j]


# Algoritmo de ordenação Bubble

def bubbleSort(lista):
    tamanho = len(lista)
    
    for j in range(tamanho-1):
        for i in range(tamanho-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                

# Algoritmo de ordenação Insertion 

def insertionSort(lista):
    tamanho = len(lista)
    for i in range(1, tamanho): # i = segundo elemento da lista
        j = i - 1 # primeiro elemento da lista
        chave = lista[i]

        while (j>=0 and lista[j] > chave):
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave
        

# Algoritmo de ordenação Merge

def mergeSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergeSort(lista, inicio, meio)
        mergeSort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1


# Algoritmo de ordenação Quick

def quickSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quickSort(lista, inicio, p-1)
        # recursivamente na sublista à direita (maiores)
        quickSort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        # j sempre avança, pois representa o elementa em análise
        # e delimita os elementos maiores que o pivô
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

