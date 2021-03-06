import pygame
from time import sleep
from pygame import mixer
from random import randint
from scipy.spatial import distance
from model import Level, VisibleObject, Charactor, Enemy, Shot, Explosion
from config import *



pygame.init()
pygame.display.set_caption(WindowCaption)
mixer.pre_init(frequency, size, channels, buffer)
mixer.init()


window = pygame.display.set_mode(
    (scr_width*scaling_factor, scr_height*scaling_factor))
screen = pygame.Surface((scr_width, scr_height))



# _________________________________MODEL_________________________________
clock = pygame.time.Clock()
xwingSound = pygame.mixer.Sound(XwingSound)
TIEfighterSound = pygame.mixer.Sound(TIEfighterSound)
TIEexplode = pygame.mixer.Sound(TIEexplodeSound)
cantinaBand = pygame.mixer.Sound(cantinaBandSound)
wilhelmscream = pygame.mixer.Sound(wilhelmscreamSound)
xWingExplode = pygame.mixer.Sound(xWingExplodeSound)
myfontS = pygame.font.Font(myfontSpath, 16)
myfontL = pygame.font.Font(myfontLpath, 50)



def switchLevel(level_finished):
    screen.fill(black)
    next_level = myfontL.render(
        f"LEVEL   {level_finished+2}", True, (255, 255, 255))
    screen.blit(next_level, ((scr_width//2)-82, scr_height//2))
    pygame.time.wait(2)
    if level_finished == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            screen.fill(black)
            end_game = myfontL.render(f"GAME FINISHED", True, (255, 255, 255))
            screen.blit(end_game, ((scr_width//2)-82, scr_height//2))


def changeLevel(level_finished, lifes_left, killed_enemies):
    switchLevel(level_finished)
    playLevel(level_finished+1, lifes_left, killed_enemies)


def playLevel(level_count, lifes_left, killed_enemies):
    level = Level(level_count=level_count)


    background = VisibleObject(screen, 0, 0)
    background.sprites = LevelSprites[level_count][0]
    charactor = Charactor(screen, 370, 280, lifes_left, killed_enemies)
    charactor.sprites = LevelSprites[level_count][1]
    shot = Shot(screen, 0, 0)
    shot.sprites = LevelSprites[level_count][2]
    enemy = Enemy(screen, 310, 1)
    enemy.sprites = LevelSprites[level_count][3]
    enemyShot = Shot(screen, 1, 100)
    enemyShot.sprites = LevelSprites[level_count][4]
    explosion = Explosion(screen, 0, 0)
    explosion.sprites = LevelSprites[level_count][5]


    charactor.lifesCount = lifes_left
    throwed = Shot.throwed
    shotVel = Shot.shotVel
    enemShotThrowed = Shot.throwed
    enemyShot.shotVel = level.levelVelocityOfEnemyShots


    run = True
    while run:
        clock.tick(40)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        if charactor.X >= scr_width-80:
            charactor.X = scr_width-80
        elif charactor.X <= 10:
            charactor.X = 10


        # CONTROLLER________________________________________________________
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:
            if charactor.prevMoveState == "right":
                charactor.charVel = charactor.charVel / 2.5
            charactor.moveState = "left"
            if charactor.charVel < 12.0:
                charactor.charVel += 0.5
        elif keys[pygame.K_RIGHT]:
            if charactor.prevMoveState == "left":
                charactor.charVel = charactor.charVel / 2.5
            charactor.moveState = "right"
            if charactor.charVel < 12.0:
                charactor.charVel += 0.5
        else:
            if charactor.charVel >= 0.5:
                charactor.charVel -= 0.5
            charactor.moveState = "stop"


        if keys[pygame.K_SPACE]:
            if throwed == False:
                xwingSound.play()
                throwed = True
                shot.X = charactor.X
                shot.Y = charactor.Y


        # WIDOK____________________________________________________________
        background.renderObject()


        if charactor.moveState == "left":
            charactor.prevMoveState = "left"
            charactor.X -= charactor.charVel
            charactor.renderObject()
        elif charactor.moveState == "right":
            charactor.prevMoveState = "right"
            charactor.X += charactor.charVel
            charactor.renderObject()
        else:
            if charactor.prevMoveState == "left":
                charactor.X -= charactor.charVel
                charactor.renderObject()
            elif charactor.prevMoveState == "right":
                charactor.X += charactor.charVel
                charactor.renderObject()
            else:
                charactor.renderObject()


        if enemy.X <= 1:
            enemy.enemTurn = "right"
        if enemy.X >= scr_width-80:
            enemy.enemTurn = "left"


        if enemy.enemTurn == "right":
            enemy.X += enemy.enemVel
            if enemy.enemAlive == True:
                enemy.renderObject()
        elif enemy.enemTurn == "left":
            enemy.X -= enemy.enemVel
            if enemy.enemAlive == True:
                enemy.renderObject()


        if throwed == True:
            shot.Y -= shotVel
            shot.renderObjectWithCorrection(5, 0)
            shot.renderObjectWithCorrection(74, 0)
            if shot.Y < 0:
                throwed = False


        if enemShotThrowed == False:
            if enemy.enemAlive == True:
                enemShotThrowed = True
                enemyShot.X = enemy.X
                enemyShot.Y = enemy.Y


        if enemShotThrowed == True:
            enemyShot.Y += enemyShot.shotVel
            enemyShot.renderObjectWithCorrection(58, 50)
            if enemyShot.Y > scr_height + randint(30, 5000):
                TIEfighterSound.play()
                enemShotThrowed = False


        if enemy.enemAlive == True:
            if throwed == True:
                if distance.euclidean((shot.X+47, shot.Y), (enemy.X+60, enemy.Y+60)) < 50:
                    explosion.X = enemy.X
                    explosion.Y = enemy.Y
                    charactor.killsCount += 1
                    print(
                        f"......Trafiłeś {charactor.killsCount} wrogów......")
                    enemy.enemAlive = False
                    TIEexplode.play()
                    enemy.enemSpawnTime = -(randint(15, 100))


        if enemShotThrowed == True:
            if distance.euclidean((charactor.X+45, charactor.Y+47), (enemyShot.X+64, enemyShot.Y+115)) < 40:
                wilhelmscream.play()
                charactor.lifesCount -= 1
                if charactor.lifesCount <= 0:
                    xWingExplode.play()
                    explosion.X = charactor.X
                    explosion.Y = charactor.Y
                    explosion.renderObject()
                    run = False


        if enemy.enemAlive == False:
            explosion.expVisible -= 1
            if explosion.expVisible >= 0:
                if explosion.expVisible == 1:
                    screen.fill(white)
                explosion.renderObject()
            if explosion.expVisible == enemy.enemSpawnTime:
                enemy.enemAlive = True
                if enemy.enemTurn == "left":
                    enemy.enemTurn = "right"
                else:
                    enemy.enemTurn = "left"
                explosion.expVisible = ExplosionVisibleTime


        score = myfontS.render(
            f"SCORE     {charactor.killsCount}", True, (255, 255, 255))
        lives = myfontS.render(
            f"LIFES     {charactor.lifesCount}", True, (255, 255, 255))
        screen.blit(score, ((scr_width//2)-150, scr_height-15))
        screen.blit(lives, ((scr_width//2)+100, scr_height-15))


        window.blit(pygame.transform.scale(
            screen, window.get_rect().size), (0, 0))
        pygame.display.update()


        if charactor.killsCount >= NextLevelLimits[level_count]:
            screen.fill(black)
            level_finished = level_count
            lifes_left = charactor.lifesCount
            killed_enemies = charactor.killsCount
            del background
            del charactor
            del shot
            del enemy
            del enemyShot
            del explosion
            changeLevel(level_finished, lifes_left, killed_enemies)


        if charactor.lifesCount <= 0:
            level.levelViewScore(window, screen, charactor.killsCount)


playLevel(0, Charactor.def_lifesCount, Charactor.def_killsCount)


pygame.quit()
