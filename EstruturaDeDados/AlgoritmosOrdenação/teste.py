import random
from algoritmos import selectionSort, bubbleSort, insertionSort, mergeSort, quickSort

any_numbers = random.sample(range(1, 1000), 42)

sortedlist = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28, 32, 34, 36, 39, 
40, 42, 87, 99, 112, 117, 90, 88, 83, 81, 77, 74, 69, 64, 64, 51, 50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 64, 51, 50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 4, 5, 7, 1]

listat = [2, 3, 4, 1] # lista quase ordenada, apenas o último elemento fora da posição correta. 

if __name__ == "__main__":
    lista = listat # pode alterar para qualquer uma das lista para teste
    print(lista)
    bubbleSort(lista)
    print("Lista ordenada: ")
    print(lista)