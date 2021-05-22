g = {}

print("Informe as listas de adjacências por linhas")
linha = input()
while (linha!=""):
    lista = linha.split(" ")
    v1 = lista[0]

    if (len(lista) == 1):
        if (v1 not in g):
            g[v1] = {'adjacencias': list([])}
        else:
            v2 = lista[1]
            if (v1 not in g):
                g[v1] = {'adjacencias': list([v2])}
            else:
                g[v1]['adjacencias'].append(v2)
            
            if(v2 not in g):
                g[v2] = {'adjacencias': list([v1])}
            else:
                g[v2]['adjacencias'].append(v1)
    linha = input()
    print(g)
