import pygame
from pygame.locals import *
from random import randint
pygame.init()
fenetre = pygame.display.set_mode((425, 480))
pygame.display.set_caption('Rei')
passe = pygame.mixer.Sound('../res/pas.wav')
ok = pygame.mixer.Sound('../res/ok.wav')
chiffre = 0
maxi_f = open('../res/score')
maxi = int(maxi_f.read())
maxi_f.close()
score = 'Score : 0     Record : {}'.format(str(maxi))
myfont = pygame.font.SysFont("Arial", 24)
score_display = myfont.render(score, 1, (255,255,0))
cadre = pygame.image.load('../res/cadre.png').convert_alpha()
cadre = pygame.transform.scale(cadre,(225,135))
end = 1
tombe = 0
tombe_cours = 0
v = 0
joueur = 0
g=1
while end:
    pygame.display.flip()
    pygame.time.Clock().tick(1000 + g)
    if(v == 0):
        fond = pygame.image.load('../res/perso/{}/background.jpg'.format(joueur)).convert()
        fond = pygame.transform.scale(fond,(425,480))
        fenetre.blit(fond,(0,0))
        fichier_nom = open('../res/perso/{}/nom.txt'.format(joueur))
        nom = str(fichier_nom.read())
        x_n = 212.5-(len(nom)*4.25)
        nom_display = myfont.render(nom, 1, (255,255,255))
        perso = pygame.image.load('../res/perso/{}/joueur.png'.format(joueur)).convert_alpha()
        perso = pygame.transform.scale(perso,(106,106))
        position_perso = perso.get_rect()
        position_perso = position_perso.move(159.5,287)
        fenetre.blit(perso,position_perso)
        fenetre.blit(cadre,(100,272.5))
        fenetre.blit(score_display,(0,0))
        fenetre.blit(nom_display,(x_n,410))
        fall = pygame.image.load('../res/perso/{}/fall.png'.format(joueur)).convert_alpha()
        fall = pygame.transform.scale(fall,(106,106))
        pos_fall = fall.get_rect()
        pos_fall.y = -320
        lose = pygame.image.load('../res/perso/{}/loose.png'.format(joueur))
        lose = pygame.transform.scale(lose, (425,425))
        dead = pygame.mixer.Sound('../res/perso/{}/dead.wav'.format(joueur))
        pas = pygame.mixer.Sound('../res/perso/{}/pass.wav'.format(joueur))
        pygame.mixer.music.load('../res/perso/{}/fond.mp3'.format(joueur))
    elif(v == 1):
        if pos_fall.y >= 480:
            chiffre = chiffre+10
            score = 'Score : {}     Record : {}'.format(chiffre, maxi)
            tombe = 0
            tombe_cours = 0
            pos_fall.x = 0
            pos_fall.y = -320
            g=g+1
        if tombe == 0:
            pos_fall = pos_fall.move(randint(0,3)*106,0)
            tombe_cours = 1
            tombe = 1
        if tombe_cours == 1:
            pos_fall = pos_fall.move(0,g)
        if(position_perso.colliderect(pos_fall) == True):
            dead.play()
            v = 2
        score_display = myfont.render(score, 1,(255,255,0))
        fenetre.blit(fond,(0,0))
        fenetre.blit(perso,position_perso)
        fenetre.blit(fall, pos_fall)
        fenetre.blit(score_display,(0,0))
    elif(v == 2):
        if(chiffre>maxi):
            change = open('../res/score', 'w')
            change.write(str(chiffre))
            change.close()
            maxi_f = open('../res/score')
            maxi = int(maxi_f.read())
            maxi_f.close()
            score = 'Score : {}     Record : {}'.format(chiffre, maxi)
            score_display = myfont.render(score, 1,(255,255,0))
        fenetre.blit(fond,(0,0))
        fenetre.blit(score_display,(0,0))
        fenetre.blit(nom_display,(x_n,40))
        fenetre.blit(lose,(0,55))
    for event in pygame.event.get():
        if event.type == QUIT:
            end = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                end = 0
            if(v == 0):
                if event.key == K_SPACE:
                    position_perso = position_perso.move(-53,87)
                    ok.play()
                    pygame.time.wait(1400)
                    pygame.mixer.music.play()
                    v = 1
                    g = 1
                if event.key == K_LEFT and joueur>0:
                    joueur -= 1
                    passe.play()
                if event.key == K_RIGHT and joueur<4:
                    joueur += 1
                    passe.play()
            if(v == 1):
                if event.key == K_LEFT and position_perso.x>0:
                    position_perso = position_perso.move(-106.5,0)
                    pas.play()
                if event.key == K_RIGHT and position_perso.x<318:
                    position_perso = position_perso.move(106,0)
                    pas.play()
            if(v == 2):
                if event.key == K_SPACE:
                    ok.play()
                    chiffre = 0
                    score = 'Score : {}     Record : {}'.format(chiffre, maxi)
                    score_display = myfont.render(score, 1,(255,255,0))
                    v = 0
pygame.quit()
