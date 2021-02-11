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
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            marcando = True        
        if event.type == pygame.MOUSEBUTTONUP:
            marcando = False
    
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
    
    pygame.draw.rect(WIN, BLACK, pygame.Rect(( (i[0] - 1) * square_w, (i[1] - 1) * square_w), (length)))

    if nodeAtual in nosPassados:
        pass
    else:
        pygame.draw.rect(WIN, BLUE, pygame.Rect(( nodeAtual['coord'][0] - 1) * square_w, (nodeAtual['coord'][1] - 1) * square_w), length)
        nosPassados.append(nodeAtual['coord'])
    
    for i in nosPassados:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(( i[0] - 1) * square_w, (i[1] - 1) * square_w), length)


    pygame.display.update()



"""
TO-DO
1. criar uma tela
2. fazer um retângulo
3. exibir ele na tela

4. fazer as linhas
5. depois colorir os retângulos vermelhos

6. pegar as coordernadas do mouse e se o botão está clicado
7. transformar em coordenadas da matriz

8. adicionar essas coordenadas em uma lista e fazer rects pretos com ela
9. essa lista será as coordenadas que o path não poderá ultrapassar -alterar na função posNos-

10. pintar de vermelho os pontos que forem para o open set
11. pintar de verde os pontos que forem para all_sect

. botão para dar start no algoritmo 

. fazer uma função para receber uma lista de coordenadas e preencher os pretos

"""
