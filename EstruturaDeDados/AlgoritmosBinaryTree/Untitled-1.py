
from aa import insere, in_order, pre_order, busca, mininum, maximum, pos_order
class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self) -> str:
        return '%s <- %s -> %s' %(self.esquerda and self.esquerda.chave,self.chave, self.direita and self.direita.chave)

raiz = NodoArvore(40)
for chave in [20, 18, 21, 13, 92]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)
in_order(raiz)
print("separação")
pos_order(raiz)
print("separção")
pre_order(raiz)
for chave in [18, 21, 0]:
    resultado = busca(raiz, chave)
    if resultado:
        print(f'busca pela chave {chave}: sucesso')
    else:
        print(f'busca pela chave {chave}: falhou')

print(mininum(raiz))
print(maximum(raiz))