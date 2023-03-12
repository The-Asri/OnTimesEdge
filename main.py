import pygame
import eventHandler
import KeyManager
import camera
import box
import border
import Player
import LevelAssets
import ImageAssets

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
cityBackground = None
ruinsBackground = None
cityWallpaper = None
ruinsWallpaper = None
paralaxFactor = 8
player = None
boxesCity = []
boxesRuins = []
currentBoxes = boxesCity
inCity = True
bufferBox = None
bufferTime = 0
switchLock = False
switchWarningTime = 8

def init():
    global screen
    global clock
    global keyManager
    global surface
    global cam
    global levelBorder
    global cityBackground
    global ruinsBackground
    global cityWallpaper
    global ruinsWallpaper
    global player

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    surface = pygame.Surface((trueWidth, trueHeight))
    pygame.display.set_caption("GameJam")
    clock = pygame.time.Clock()
    keyManager = KeyManager.KeyManager()
    player = Player.Player(0, 0)
    levelBorder = border.Border(0, 0)
    cityWallpaper = ImageAssets.loadImage(1)
    ruinsWallpaper = ImageAssets.loadImage(2)
    cityBackground = ImageAssets.loadImage(3)
    ruinsBackground = ImageAssets.loadImage(4)
    LevelAssets.loadLevel(1, boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)
    cam = camera.Camera(trueWidth, trueHeight, levelBorder, player)


def main():
    eventHandler.eventHandler(keyManager)

    update()
    draw()

    pygame.display.update()
    clock.tick(30)


def update():
    global bufferBox
    global bufferTime
    global inCity
    global switchLock
    global currentBoxes

    if keyManager.key_escape:
        pygame.quit()
        exit()
    if keyManager.key_reset:
        LevelAssets.loadLevel(1, boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)
        inCity = True
        currentBoxes = boxesCity
    if keyManager.key_switch and not switchLock:
        switch()
    if not keyManager.key_switch:
        switchLock = False

    player.update(currentBoxes, keyManager)
    cam.update(trueWidth, trueHeight, levelBorder)

    if bufferTime > 0:
        bufferTime -= 1
        if bufferTime <= 0:
            bufferBox = None

def draw():
    surface.fill("Black")
    # draw below here!

    if inCity:
        surface.blit(cityWallpaper, (-cam.x / paralaxFactor, -cam.y / paralaxFactor))
        #surface.blit(cityBackground, (-cam.x, -cam.y))
    else:
        surface.blit(ruinsWallpaper, (-cam.x / paralaxFactor, -cam.y / paralaxFactor))
        #surface.blit(ruinsBackground, (-cam.x, -cam.y))

    for b in currentBoxes:
        b.draw(surface, cam)
        pass

    if bufferBox is not None:
        bufferBox.draw(surface, cam)

    player.draw(surface, cam)

    # dont edit this code below
    upscaled = pygame.transform.scale_by(surface, upscale)
    screen.blit(upscaled, (0, 0))

def switch():
    global switchLock
    global inCity
    global bufferBox
    global bufferTime
    global currentBoxes

    switchLock = True

    otherBoxes = None
    if inCity:
        otherBoxes = boxesRuins
    else:
        otherBoxes = boxesCity
    for b in otherBoxes:
        if b.isColliding(player.getHitbox()):
            bufferBox = b
            bufferTime = switchWarningTime
            return
    inCity = not inCity
    currentBoxes = otherBoxes

init()

while True:
    main()
