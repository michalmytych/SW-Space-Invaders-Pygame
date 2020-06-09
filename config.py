import pygame

scr_width = 750
scr_height = 400
scaling_factor = 2
white = (255,255,255)
black = (0,0,0)
WindowCaption = 'Star Wars Space Invaders'


frequency = 44100 
size = -16 
channels = 2 
buffer = 2048


CharacterLifes = 15
CharacterVelocity = 0
KilledEnemiesDefault = 0
EnemyVelocity = 7
EnemySpawnTime = -50
BlasterVelocity = 30
ExplosionVisibleTime = 6


numberOflevels = 4 
NextLevelLimits = [
    20,             # Level 1
    35,             # Level 2
    65,             # Level 3
    125             # Level 4
]


LevelSprites = [
        [[pygame.image.load("assets/space.png")],       # Level 1
    [pygame.image.load("assets/royal.png")],
    [pygame.image.load("assets/redshot.png")],
    [pygame.image.load("assets/vulture.png")],
    [pygame.image.load("assets/redshot.png")],
    [pygame.image.load("assets/explosionPix.png")]],
        [[pygame.image.load("assets/space.png")],       # Level 2
    [pygame.image.load("assets/xwing.png")],
    [pygame.image.load("assets/redshot.png")],
    [pygame.image.load("assets/tiefighter.png")],
    [pygame.image.load("assets/greenshot.png")],
    [pygame.image.load("assets/explosionPix.png")]],
        [[pygame.image.load("assets/space.png")],       # Level 3
    [pygame.image.load("assets/rebelBomber.png")],
    [pygame.image.load("assets/redshot.png")],
    [pygame.image.load("assets/imperialBomber.png")],
    [pygame.image.load("assets/greenshot.png")],
    [pygame.image.load("assets/explosionPix.png")]],
        [[pygame.image.load("assets/space.png")],       # Level 4
    [pygame.image.load("assets/falcon.png")],
    [pygame.image.load("assets/redshot.png")],
    [pygame.image.load("assets/slaveOne.png")],
    [pygame.image.load("assets/greenshot.png")],
    [pygame.image.load("assets/explosionPix.png")]]
    ]



XwingSound = 'assets/XWingFire.wav'
TIEfighterSound = 'assets/TIEfighterFire.wav'
TIEexplodeSound = 'assets/TIEexplode.wav'
cantinaBandSound = 'assets/cantinaBand.wav'
wilhelmscreamSound = 'assets/wilhelmscream.wav'
xWingExplodeSound = 'assets/xWingExplode.wav'



myfontSpath = "assets/arcadeClassic.TTF"
myfontLpath = "assets/arcadeClassic.TTF"