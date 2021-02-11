# Path Finding Algorithm
# Mapear os possíveis nós em volta do atual
# Preencher o G H, F e L (last) deles
# Colocar os nós no Open-Set
# Avaliar o próximo nó que tiver menor F

# ELEMENTOS
# nós: linhas em uma tabela com colunas sendo: id/coordenadas, g, h, f, l.
# nó final e inicial: coordenadas

# Considerando um cenário inicial de 4x4
# x aumenta indo para a direita, e y aumenta indo para baixo, a origem(0,0) é no canto superior esquerdo. Semelhante ao PYGAME 

import math
import time

noInicial = (1,1)
nodeInicial = {"coord": noInicial, "g": 0, "h": 10000, "f":10000, "l": "inicio" }
noFinal = (3,4)
nodeAtual = nodeInicial
all_nodes = [nodeInicial]
fila = []
coords_nos = [noInicial]


def possiveis_nos(no, rg = 3):
    # recebe a coordenada do nó
    # retorna uma lista com as coordenadas dos possíveis nós
    x = no[0]
    y = no[1]
    nos = []
    for i in range(rg):
        for j in range(rg):
            # pega as coordenadas dos nós em volta do nó atual
            new_x = (x-1) + i
            new_y = (y-1) + j
            # verifica se o nó em volta tá dentro dos limites da matriz
            if (new_x > 0 and new_x <= 4): # verifica se o nó está dentro dos limites da matrix em x
                if (new_y > 0 and new_y <= 4): # verifica se está dentro dos limites em y
                    nos.append((new_x, new_y))
                    
                    if(x== new_x and y==new_y): # não adiciona o novo nó, se ele tiver as coordenadas do nó atual
                        nos.pop()
    return nos

def formar_node(nos):
    # recebe uma lista de nos
    # dá atributos para ele, o transformando em node
    # estou considerando que um nó seja apenas as coordenadas de um ponto
    # e o nó é promovido a node após ter atributos
    
    nodes = []
    # print(nos)
    for no in nos:
        h = distancia(no)
        if not (no in coords_nos): # se o nó ser um ponto que ainda não é node
            coords_nos.append(no)
            g = nodeAtual['g'] + 1
            l = nodeAtual
        else:
            for i in all_nodes:
                if(i["coord"] == no):
                    index = all_nodes.index(i)
                    nodeAntigo = all_nodes.pop(index)
            if(nodeAtual['g'] + 1 <= nodeAntigo['g']):
                g = nodeAtual['g'] + 1
                l = nodeAtual 
            else:
                g = nodeAntigo['g']  
                l = nodeAntigo

        f = g + h
        node = {"coord": no, "g": g, "h": h, "f": f, "l": l}
        all_nodes.append(node)
        nodes.append(node)

    return nodes


def distancia(no):
    dist_x = (noFinal[0] - no[0])**2
    dist_y = (noFinal[1] - no[1])**2
    return math.sqrt(dist_x + dist_y)


def mostrar_caminho(node):
    while (node['l'] != "inicio"):
        print(node['coord'])
        node = node['l']
    print(node['coord'])


while True:
    if (nodeAtual["coord"] == noFinal):
        print('achooooouu')
        mostrar_caminho(nodeAtual)
        break
    
    posNos = possiveis_nos(nodeAtual["coord"])
    posNodes = formar_node(posNos)

    for i in posNodes:
        if i in fila:
            pass
        else:
            fila.append(i)
    min_f = 1000

    for i in fila:
        if i['f'] <= min_f:
            min_f = i['f']
            nodeAtual = i
    # print(nodeAtual['coord'])