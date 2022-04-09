from curses import KEY_UP
from turtle import Screen
import pygame
import time 
import random


ventana = pygame.display.set_mode((500, 500))

#colores!
pink = pygame.Color(255, 56, 100)
blue = pygame.Color(0, 121, 145)
purple = pygame.Color(52, 0, 104)
white = pygame.Color(255, 252, 249)

pygame.init()
pygame.font.init()

#dados
uno = [
        [white, white, white, white, white, white, white],
        [white, white, white, white, white, white, white],
        [white, white, white, white, white, white, white],
        [white, white, white, pink, white, white, white],
        [white, white, white, white, white, white, white],
        [white, white, white, white, white, white, white],
        [white, white, white, white, white, white, white]
    ]

dos = [
        [white, white, white, white, white, white, white],
        [white, white, white, pink, white, white, white],
        [white, white, white, white, white, white, white],
        [white, white, white, white, white, white, white],
        [white, white, white, white, white, white, white],
        [white, white, white, pink, white, white, white],
        [white, white, white, white, white, white, white]
    ]

tres = [
        [white, white, white, white, white, white, white],
        [white, pink, white, white, white, white, white],
        [white, white, white, white, white, white, white],
        [white, white, white, pink, white, white, white],
        [white, white, white, white, white, white, white],
        [white, white, white, white, white, pink, white],
        [white, white, white, white, white, white, white]
    ]

cuatro = [
        [white, white, white, white, white, white, white],
        [white, pink, white, white, white, pink, white],
        [white, white, white, white, white, white, white],
        [white, white, white, white, white, white, white],
        [white, white, white, white, white, white, white],
        [white, pink, white, white, white, pink, white],
        [white, white, white, white, white, white, white]
    ]

cinco = [
        [white, white, white, white, white, white, white],
        [white, pink, white, white, white, pink, white],
        [white, white, white, white, white, white, white],
        [white, white, white, pink, white, white, white],
        [white, white, white, white, white, white, white],
        [white, pink, white, white, white, pink, white],
        [white, white, white, white, white, white, white]
    ]

seis = [
        [white, white, white, white, white, white, white],
        [white, pink, white, white, white, pink, white],
        [white, white, white, white, white, white, white],
        [white, pink, white, white, white, pink, white],
        [white, white, white, white, white, white, white],
        [white, pink, white, white, white, pink, white],
        [white, white, white, white, white, white, white]
    ]


#texto
myfont = pygame.font.SysFont('Calibri', 20)
win = myfont.render('You Win!', False, white)
lose = myfont.render('You Lose!', False, white)
tie = myfont.render("It's a tie", False, white)
restart = myfont.render("Press R to restart...", False, white)

textRect1 = win.get_rect()
textRect2 = lose.get_rect()
textRect3 = tie.get_rect()
textRect4 = restart.get_rect()

textRect1.center = (250//2, 100//2)
textRect2.center = (250//2, 100//2)
textRect3.center = (250//2, 100//2)
textRect4.center = (250//2, 100//2)

pygame.display.set_caption('Dados')
ventana.fill(blue)

pygame.display.flip()

def generate_dado(usuario, ai, c, temp):
    
    dado_uno = [100, 200]
    for i in usuario:
        for j in i:
            pygame.draw.rect(ventana, j, pygame.Rect(dado_uno[0]+c, dado_uno[1]+temp, 10, 10))
            c+=10
        temp+=10
        c = 0

    dado_dos = [300, 200]
    temp = 0
    for i in ai:
        for j in i:
            pygame.draw.rect(ventana, j, pygame.Rect(dado_dos[0]+c, dado_dos[1]+temp, 10, 10))
            c+=10
        temp+=10
        c = 0

    
    pygame.display.update()
    

def game():

    usuario = random.randint(1, 6)
    ai = random.randint(1, 6)
    c = random.randint(1, 1)
    
    if usuario == 1:
        score_usu = uno
    elif usuario == 2:
        score_usu = dos
    elif usuario == 3:
        score_usu = tres
    elif usuario == 4:
        score_usu = cuatro
    elif usuario == 5:
        score_usu = cinco
    else:
        score_usu = seis
    
    if ai == 1:
        score_ai = uno
    elif ai == 2:
        score_ai = dos
    elif ai == 3:
        score_ai = tres
    elif ai == 4:
        score_ai = cuatro
    elif ai == 5:
        score_ai = cinco
    else:
        score_ai = seis
        
    generate_dado(score_usu, score_ai, c, c)

    time.sleep(2)

    if usuario > ai:
        pass
        #You Win!
        print("You Win!")
        ventana.blit(win,(200,300))
    elif usuario < ai:
        pass
        print("You lose!")
        ventana.blit(lose,(200,300))
    else:
        pass
        print("It's a tie!")
        ventana.blit(tie,(200,300))


activo = True
cont = 0
while activo:
    
    if cont == 0:
        game()
        cont = 1
    
    ventana.blit(restart,(150,400))

    for event in pygame.event.get():    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print('Restarting...')
                time.sleep(2)
                ventana.fill(blue)
                game()

        elif event.type == pygame.QUIT:
            activo = False
        
        pygame.display.update()