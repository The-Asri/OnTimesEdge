import pygame
import eventHandler
import KeyManager
import camera
import box
import border
import Player
import LevelAssets

screen = None
surface = None
clock = None
keyManager = None
cam = None
trueWidth = 150
trueHeight = 100
upscale = 6
width = trueWidth * upscale
height = trueHeight * upscale
levelBorder = None
player = None
boxesCity = []
boxesRuins = []
inCity = True
bufferBox = None
bufferTime = None
switchLock = False

def init():
    global screen
    global clock
    global keyManager
    global surface
    global cam
    global levelBorder
    global player

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    surface = pygame.Surface((trueWidth, trueHeight))
    pygame.display.set_caption("GameJam")
    clock = pygame.time.Clock()
    keyManager = KeyManager.KeyManager()
    player = Player.Player(0, 0)
    levelBorder = border.Border(0, 0)
    LevelAssets.loadLevel(1, boxesCity, boxesRuins, levelBorder, player)
    cam = camera.Camera(trueWidth, trueHeight, levelBorder, player)


def main():
    global inCity
    global bufferBox
    global bufferTime
    global switchLock

    eventHandler.eventHandler(keyManager)
    update()
    draw()
    pygame.display.update()
    clock.tick(30)
    if keyManager.key_escape:
        pygame.quit()
        exit()
    if keyManager.key_reset:
        LevelAssets.loadLevel(1, boxesCity, boxesRuins, levelBorder, player)
        inCity = True
    if keyManager.key_switch and not switchLock:
        switchLock = True
        if inCity:
            for b in boxesRuins:
                if b.isColliding(player):
                    bufferBox = b
                    bufferTime = 0
                    break
            else:
                inCity = False
        else:
            for b in boxesCity:
                if b.isColliding(player):
                    bufferBox = b
                    bufferTime = 0
                    break
            else:
                inCity = True
    if not keyManager.key_switch:
        switchLock = False


def update():
    print(inCity)
    if inCity:
        player.update(boxesCity, keyManager)
    else:
        player.update(boxesRuins, keyManager)
    cam.update(trueWidth, trueHeight, levelBorder)

def draw():
    global bufferBox
    global bufferTime

    surface.fill("Black")
    # draw below here!

    if inCity:
        for b in boxesCity:
            b.draw(surface, cam)
    else:
        for b in boxesRuins:
            b.draw(surface, cam)

    if bufferBox is not None:
        bufferBox.draw(surface, cam)
        bufferTime += 1
        if bufferTime == 8:
            bufferBox = None
            bufferTime = None

    player.draw(surface, cam)

    # dont edit this code below
    upscaled = pygame.transform.scale_by(surface, upscale)
    screen.blit(upscaled, (0, 0))

init()

while True:
    main()
