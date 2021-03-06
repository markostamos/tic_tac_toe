
import pygame,sys
from Game import Game
from constants import *
from helpers import *
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("MINIMAX TIC-TAC-TOE ")
screen.fill(BG)

draw_grid(screen)

game = Game("O")
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            restart(screen=screen,game=game)
            game_over = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            row,col = get_row_col(event,event.pos[0],event.pos[1])
            result= game.play(row,col)
            if result is None:
                continue
            draw_figures(screen,game.board)
            if result["winner"] is not None:
                if result["winner"]=="DRAW":
                    game_over = True
                else:
                     draw_winner(screen,player = result["winner"],pos=result["pos"],type=result["type"])
                     game_over = True
        

    pygame.display.update()


