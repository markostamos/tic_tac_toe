import pygame
from constants import *

def draw_grid(screen):
    #horizontal
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),LINE_WIDTH)
    
    #vertical
    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(400,0),(400,600),LINE_WIDTH)

def get_row_col(event,mouseX,mouseY):
    mouseX = event.pos[0]
    mouseY = event.pos[1]
    row = int(event.pos[1]/R)
    col = int(event.pos[0]/C)
    return row,col

def draw_figures(screen,board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col]=="O":
                pygame.draw.circle(screen,CIRCLE_COLOR,(int(col*C+C/2),int(row*R+R/2)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col]=="X":
                pygame.draw.line(screen,CROSS_COLOR,(int(col*C+SPACE),int(row*R+R-SPACE)),(int(col*C+C-SPACE),int(row*R+SPACE)),CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(int(col*C+SPACE),int(row*R+SPACE)),(int(col*C+C-SPACE),int(row*R+R-SPACE)),CROSS_WIDTH)

def draw_winner(screen,player,pos,type):
    
    if type=="horizontal":
        draw_horizontal_line(screen,row=pos,player=player)
    elif type=="vertical":
        draw_vertical_line(screen,col = pos,player=player)
    elif type=="asc":
        draw_diagonal_line(screen,asc=True,player=player)
    else:
        draw_diagonal_line(screen,asc=False,player=player)


def draw_vertical_line(screen,col,player):
    posX = col*C+C/2

    if player=="O":
        color = CIRCLE_COLOR
    if player=="X":
        color = CROSS_COLOR
    
    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)

def draw_horizontal_line(screen,row,player):
    posY = row*R+R/2

    if player=="O":
        color = CIRCLE_COLOR
    if player=="X":
        color = CROSS_COLOR
    
    pygame.draw.line(screen,color,(15,posY),(WIDTH-15,posY),15)
def draw_diagonal_line(screen,player,asc):
    if player=="O":
        color = CIRCLE_COLOR
    if player=="X":
        color = CROSS_COLOR
    if asc ==True:
        pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)
    elif asc==False:
        pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)


def restart(screen,game):
    screen.fill(BG)
    draw_grid(screen)
    game.restart()
   