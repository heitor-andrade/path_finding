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
import random
random.seed(4)


WIDTH = 50
LENGTH = 50
noInicial = (5,1)
nodeInicial = {"coord": noInicial, "g": 0, "h": 10000, "f":10000, "l": "inicio" }
noFinal = (50,50)
nodeAtual = nodeInicial
all_nodes = [nodeInicial]
fila = []
coords_nos = [noInicial]


def possiveis_nos(no, rg = 3):
    # recebe a coordenada do nó
    # retorna uma lista com as coordenadas dos possíveis nós
    proibidos = [(0,0), (2,0), (0,2), (2,2)]
    x = no[0]
    y = no[1]
    nos = []
    for i in range(rg):
        for j in range(rg):
            # pega as coordenadas dos nós em volta do nó atual
            
            new_x = (x-1) + i
            new_y = (y-1) + j
            # verifica se o nó em volta tá dentro dos limites da matriz
            if not ((new_x, new_y) in nosPassados or (new_x, new_y) in blackSquares):
                if (new_x > 0 and new_x <= QTDE_SQUARES): # verifica se o nó está dentro dos limites da matrix em x
                    if (new_y > 0 and new_y <= QTDE_SQUARES): # verifica se está dentro dos limites em y
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
    for no in nos:
        h = distancia(no)
        if not (no in coords_nos): # se o nó ser um ponto que ainda não é node
            coords_nos.append(no)
            g = nodeAtual['g'] + 1
            l = nodeAtual['coord']
        else:
            for i in all_nodes:
                if(i["coord"] == no):
                    index = all_nodes.index(i)
                    nodeAntigo = all_nodes.pop(index)
            if(nodeAtual['g'] + 1 <= nodeAntigo['g']):
                g = nodeAtual['g'] + 1
                l = nodeAtual['coord']
            else:
                g = nodeAntigo['g']  
                l = nodeAntigo['coord']

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

min_f = 1000

####################################################################3
# interface

import pygame

WIDTH, HEIGHT = 600, 600
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path Finding Algorithm")

# matriz 4x4
QTDE_SQUARES = 50
square_w = WIDTH/QTDE_SQUARES
length = (square_w,square_w)

blackSquares = []
nosPassados = []

WIN.fill(WHITE)
for i in range(QTDE_SQUARES - 1):
    pygame.draw.line(WIN, BLACK, ((i + 1)*square_w, 0), ((i+1)*square_w, HEIGHT))
    pygame.draw.line(WIN, BLACK, (0, (i + 1)*square_w), (WIDTH, (i+1)*square_w))

clock = pygame.time.Clock()
marcando = False
started = False
posNos = []

while True:
    if(started):
        print(len(fila))
        posNos = possiveis_nos(nodeAtual["coord"])
        posNodes = formar_node(posNos)

        if nodeAtual['coord'] == noFinal:
            print("opa, achei!")
            time.sleep(3)
            break

        for i in posNodes:
            if i in fila:
                pass
            else:
                fila.append(i)
        
        min_f = 100
        for i in fila:
            if i['coord'] in nosPassados:
                fila.remove(i)
                continue

            if i['f'] <= min_f:
                min_f = i['f']
                nodeAtual = i

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            marcando = True        
        if event.type == pygame.MOUSEBUTTONUP:
            marcando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                started = True
            if event.key == pygame.K_a:
                print(fila)
                time.sleep(5)
    
    if marcando:
        x, y = pygame.mouse.get_pos()
        coord_x = x//square_w + 1
        coord_y = y//square_w + 1

        if (coord_x, coord_y) in blackSquares:
            pass
        else:
            blackSquares.append((coord_x,coord_y))
            pygame.draw.rect(WIN, BLACK, pygame.Rect(( (coord_x - 1) * square_w, (coord_y - 1) * square_w), (length)))

    for i in posNos:
        pygame.draw.rect(WIN, BLACK, pygame.Rect(( (i[0] - 1) * square_w, (i[1] - 1) * square_w), (length)))

    for i in nosPassados:
        pygame.draw.rect(WIN, GREEN, pygame.Rect((( i[0] - 1) * square_w, (i[1] - 1) * square_w), length) )
    
    if nodeAtual in nosPassados:
        pass
    else:
        nosPassados.append(nodeAtual['coord'])
    
    pygame.draw.rect(WIN, BLUE, pygame.Rect((( nodeAtual['coord'][0] - 1) * square_w, (nodeAtual['coord'][1] - 1) * square_w), (length)))


    pygame.display.update()