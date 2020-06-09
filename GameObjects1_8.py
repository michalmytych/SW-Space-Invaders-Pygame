# ___________________Lib___________________
from GameConfig import *
pygame.init()



class Game:
    myfontS = pygame.font.Font(myfontSpath, 16)
    myfontL = pygame.font.Font(myfontLpath, 30)
    xwingSound = pygame.mixer.Sound(XwingSound)
    TIEfighterSound = pygame.mixer.Sound(TIEfighterSound)
    TIEexplode = pygame.mixer.Sound(TIEexplodeSound)
    cantinaBand = pygame.mixer.Sound(cantinaBandSound)
    wilhelmscream = pygame.mixer.Sound(wilhelmscreamSound)
    xWingExplode = pygame.mixer.Sound(xWingExplodeSound)



class Level(Game):
    def __init__(self,
        level_count=0,
        levelVelocityOfEnemyShots= 25,
        enemiesLevelVelocity= 7,
        levelEnemySpawnTime = -50):
        self.level_count = level_count 
        self.levelVelocityOfEnemyShots = levelVelocityOfEnemyShots
        self.enemiesLevelVelocity = enemiesLevelVelocity
        self.levelEnemySpawnTime = levelEnemySpawnTime 


    def levelViewScore(self, window, screen, score):
        self.cantinaBand.play()
        not_quitted = True   
        while(not_quitted):
            end_score = self.myfontL.render(f"YOUR SCORE   {score}", True, (255,255,255))
            screen.blit(end_score, ((scr_width//2)-82, scr_height//2))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    not_quitted = False
            
            window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
            pygame.display.update()



class VisibleObject:
    def __init__(self, screen, X, Y):
        self.screen = screen
        self.X = X
        self.Y = Y
        self.sprites = []
    
    def renderObject(self, frame=0):
        self.screen.blit(self.sprites[frame], (self.X, self.Y))

    def renderObjectWithCorrection(self, correction_x, correction_y, frame=0):
        self.screen.blit(self.sprites[frame], (self.X+correction_x, self.Y+correction_y))



class Charactor(VisibleObject):
    def __init__(self, screen, X, Y, lifesCount, killsCount):
        self.screen = screen
        self.X = X
        self.Y = Y
        self.sprites = []
        self.lifesCount = lifesCount
        self.killsCount = killsCount
    

    def renderObject(self, frame=0):
        self.screen.blit(self.sprites[frame], (self.X, self.Y))


    charVel = CharacterVelocity
    moveState = "stop"
    prevMoveState = "stopping"
    def_lifesCount = 15
    def_killsCount = 0



class Enemy(VisibleObject):
    enemVel = EnemyVelocity
    enemTurn = "left"
    enemAlive = True
    enemSpawnTime = EnemySpawnTime

        

class Shot(VisibleObject):
    throwed = False
    shotVel = BlasterVelocity



class Explosion(VisibleObject):
    expVisible = ExplosionVisibleTime







