def in_order(raiz): # caminha pela arvore in-order primeiro a esquerda, depois atual, depois final
    if not raiz:
        return 
    if raiz.esquerda != None:
        in_order(raiz.esquerda)
    print(raiz.chave)
    if raiz.direita != None:
        in_order(raiz.direita)

def pos_order(raiz): # pirmeiro a esquerda, depois a direita, depois o nó atual
    if not raiz:
        return
    if raiz.esquerda != None:
        pos_order(raiz.esquerda)
    if raiz.direita != None:
        pos_order(raiz.direita)
    print(raiz.chave)

def pre_order(raiz): # primeiro o nó atual, depois a esquerda e depois a direita
    if not raiz:
        return
    else:
        print(raiz.chave)
    if raiz.esquerda != None:
        pre_order(raiz.esquerda)
    if raiz.direita != None:
        pre_order(raiz.direita)
        
def insere(raiz, nodo): # insere um nó 
    if raiz is None:
        raiz = nodo
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)

def busca(raiz, chave): # realiza a busca de um nó
    if raiz is None:
        return None
    elif raiz.chave == chave:
        return chave
    if raiz.chave < chave:
        return busca(raiz.direita, chave)
    else:
        return busca(raiz.esquerda, chave)

def mininum(raiz): # mininum
    nodo = raiz
    while nodo.esquerda is not None:
        nodo = nodo.esquerda
    else:
        return nodo.chave

def maximum(raiz): # maximun
    nodo = raiz
    while nodo.direita is not None:
        nodo = nodo.direita
    else:
        return nodo.chave




