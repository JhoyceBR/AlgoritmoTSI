
class Node(): # cria nó 
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.pai = None

    def __str__(self) -> str:
        return str(self.chave)

class Tree(): # inicia a arvore com o nó raiz
    def __init__(self):
        self.raiz = None # raiz começa None


    def TreeInsert(self, chave, node=None): # insere um nó na árvore
        
        if (node is None):
            node = self.raiz

        if (self.raiz is None):
            self.raiz = Node(chave)

        else:
            if (chave <= node.chave):
                if (node.esquerda is None):
                    node.esquerda = Node(chave)

                else:
                    return self.TreeInsert(chave, node=node.esquerda)
            else:
                if (node.direita is None):
                    node.direita = Node(chave)

                else:
                    return self.TreeInsert(chave, node=node.direita)


    def tree_transplant(self, u, v): # transplanta uma parte 

        if (u.pai == None):
            self.raiz = v
        elif (u.pai.esquerda == u):
            u.pai.esquerda = v
        else:
            u.pai.direita = v
        
        if (v != None):
            v.pai = u.pai


    def tree_remove(self, z): # remove uma parte

        if (z.esquerda == None):
            self.tree_transplant(z, z.direita)
        elif (z.direita == None):
            self.tree_transplant(z, z.esquerda)
        else:
            y = self.minumum(z.direita)

            if(y.pai!=z):
                self.tree_transplant(y, y.direita)
                y.direita = z.direita
                y.direita.pai = y
            self.tree_transplant(z, y)
            y.esquerda = z.esquerda
            y.esquerda = z.esquerda
            y.esquerda.pai = y


    def interative_tree_search(self, chave):

        if (self.raiz == None):
            return None
        vertice = self.raiz

        while (vertice != None and vertice.chave != int(chave)):
            if (int(chave) < vertice.chave):
                vertice = vertice.esquerda
            else:
                vertice = vertice.direita
        
        return vertice

    def inorder_tree_walk(self, vertice=None): # esquerda, raiz, direita

        if (self.raiz == None):
            return
        if (vertice == None): # começa na raiz
            vertice = self.raiz
        if (vertice.esquerda != None):
            self.inorder_tree_walk(vertice = vertice.esquerda)
        print(vertice) # meio
        if (vertice.direita != None):
            self.inorder_tree_walk(vertice = vertice.direita)

        return vertice


    def decrescente_tree_walk(self, vertice=None):

        if (self.raiz == None):
            return
        if (vertice == None):
            vertice = self.raiz
        if (vertice.direita != None):
            self.decrescente_tree_walk(vertice = vertice.direita)
        print(vertice)
        if (vertice.esquerda != None):
            self.decrescente_tree_walk(vertice = vertice.esquerda)
        
        return vertice


    def preorder_tree_walk(self, vertice=None): # raiz, esquerda, direita

        if (self.raiz == None):
            return
        if (vertice == None):
            vertice = self.raiz
        print(vertice)
        if (vertice.esquerda != None):
            self.preorder_tree_walk(vertice=vertice.esquerda)
        if (vertice.direita != None):
            self.preorder_tree_walk(vertice=vertice.direita)
        return vertice


    def posorder_tree_walk(self, vertice=None): # esqueda, direita, raiz

        if (self.raiz == None):
            return
        if (vertice == None):
            vertice = self.raiz
        if (vertice.esquerda != None):
            self.posorder_tree_walk(vertice=vertice.esquerda)
        if (vertice.direita != None):
            self.posorder_tree_walk(vertice=vertice.direita)
        print(vertice)
        
        
    def minimum(self, vertice=None):
        if vertice is None:
            vertice = self.raiz
        if vertice.direita is not None:
            vertice = vertice.direita
        else:
            return vertice
        
        if vertice.esquerda is not None:
            return self.minimum(vertice=vertice.esquerda)
        else:
            return vertice
        

    def maximum(self, vertice=None):
        if (self.raiz == None):
            return None
        if (vertice == None):
            vertice = self.raiz

        while (vertice.direita != None):
            vertice = vertice.direita
        return vertice


    # consertar função minumum e maximum
    def tree_sucessor(self, vertice):

        if (vertice.direita is not None):
            return self.minimum(vertice=vertice.direita)
        parent = vertice.pai
        child = vertice

        while (parent != None and child==parent.direita):
            child = parent
            parent = child.parent
            
        return parent

    def tree_predecessor(self, vertice):

        if (vertice.esquerda is not None):
            return self.maximum(vertice=vertice.esquerda)
        parent = vertice.pai
        child = vertice

        while (parent is not None and child is parent.esquerda):
            child = parent
            parent = child.parent

        return parent


arvore = Tree()
arvore.TreeInsert(10)
arvore.TreeInsert(13)
arvore.TreeInsert(14)
arvore.TreeInsert(8)
arvore.TreeInsert(9)
arvore.TreeInsert(7)
arvore.TreeInsert(11)
arvore.TreeInsert(2)
arvore.TreeInsert(72)
#print(arvore.interative_tree_search(7))
#arvore.posorder_tree_walk()
#arvore.inorder_tree_walk()
#arvore.decrescente_tree_walk()
#arvore.preorder_tree_walk()
#print(arvore.maximum())
#arvore.tree_sucessor(10)
arvore.minimum(10)