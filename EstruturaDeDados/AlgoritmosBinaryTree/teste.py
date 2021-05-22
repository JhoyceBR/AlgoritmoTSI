from binaryTree import treeInsert
# Código de ABB 

class vertice: # calcula a chave e cria payload
    def __init__(self, key, payload): 
        self.key = int(key)
        self.payload = payload
        self.pai = None
        self.esquerdo = None
        self.direito = None
    def __str__(self): # converte pra inteiro na hora da impressão
        return str(self.key) + " " + str(self.payload)

class tree: # TAD da árvore
    def __init__(self):
        self.raiz = None
        self.count = 0 # número de vertices da árvore

if __name__ == "__main__":
    treeInsert(3)
    treeInsert(2)
    treeInsert(5)



