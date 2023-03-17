import pygame
from pygame import mixer
import eventHandler
from sys import exit
import KeyManager
import camera
import box
import border
import Player
import LevelAssets
import ImageAssets
import SoundAssets
import intro


class Background:
    def __init__(self):
        self.cityBackground = None
        self.ruinsBackground = None


screen = None
surface = None
clock = None
keyManager = None
soundHandler = None
cam = None
trueWidth = 260
trueHeight = 160
upscale = 5
width = trueWidth * upscale
height = trueHeight * upscale
background = Background()
cityWallpaper = None
ruinsWallpaper = None
parallaxFactor = 4
player = None
levelBorder = None
boxesCity = []
boxesRuins = []
currentBoxes = boxesCity
inCity = True
bufferBox = None
bufferTime = 0
switchLock = False
resetLock = False
switchWarningTime = 8
currentLevel = 1
levelCount = 4
fps = 30
ticks = 0
ticking = False
winScreen = False

renderLevel = False


def init():
    global screen
    global clock
    global keyManager
    global soundHandler
    global surface
    global cam
    global levelBorder
    global background
    global cityWallpaper
    global ruinsWallpaper
    global player

    pygame.init()
    pygame.display.set_icon(ImageAssets.loadImage(14))
    soundHandler = SoundAssets.SoundHandler()
    soundHandler.playBackground()
    screen = pygame.display.set_mode((width, height))
    surface = pygame.Surface((trueWidth, trueHeight))
    pygame.display.set_caption("On Time's Edge")
    clock = pygame.time.Clock()
    keyManager = KeyManager.KeyManager()
    player = Player.Player(0, 0)
    levelBorder = border.Border(0, 0)
    cityWallpaper = ImageAssets.loadImage(1)
    ruinsWallpaper = ImageAssets.loadImage(2)
    background.cityBackground = ImageAssets.loadImage(3)
    background.ruinsBackground = ImageAssets.loadImage(4)

    intro.intro(screen, surface, cityWallpaper, ruinsWallpaper, trueWidth, trueHeight, upscale, clock, keyManager)

    LevelAssets.loadLevel(currentLevel, boxesCity, boxesRuins, levelBorder, background, player)
    cam = camera.Camera(trueWidth, trueHeight, levelBorder, player)
    if renderLevel:
        saveLevel()
        quitGame()


def main():
    eventHandler.eventHandler(keyManager)

    update()
    draw()

    pygame.display.update()
    clock.tick(fps)


def update():
    global bufferBox
    global bufferTime
    global switchLock
    global resetLock
    global ticks
    global ticking
    global currentLevel
    global winScreen

    if winScreen:
        if keyManager.key_reset:
            fullReset()
            winScreen = False
    else:
        if ticking:
            ticks += 1
        else:
            if keyManager.key_left or keyManager.key_right or keyManager.key_jump:
                ticking = True

        if keyManager.key_reset and not resetLock:
            reset(True)
        if keyManager.key_fullReset and not resetLock:
            fullReset()
        if (keyManager.key_switch1 or keyManager.key_switch2) and not switchLock:
            switch()

        if not keyManager.key_reset and not keyManager.key_fullReset:
            resetLock = False
        if not (keyManager.key_switch1 or keyManager.key_switch2):
            switchLock = False

        player.update(currentBoxes, keyManager, soundHandler)
        if player.isDead:
            reset(True)
        cam.update(trueWidth, trueHeight, levelBorder)

    if bufferTime > 0:
        bufferTime -= 1
        if bufferTime <= 0:
            bufferBox = None

    testBorder()

    if keyManager.key_escape:
        quitGame()


def draw():
    surface.fill("Black")
    # draw below here!
    if winScreen:
        surface.blit(cityWallpaper, (-cam.x / parallaxFactor, -cam.y / parallaxFactor))
        font = pygame.font.SysFont(None, 20)
        img = font.render("Time: " + str(int(ticks / fps * 100) / 100) + " Seconds", False, "Yellow")
        surface.blit(img, (trueWidth / 2 - 60, trueHeight / 2 - 10))
        img = font.render("Press [R] to try again", False, "Yellow")
        surface.blit(img, (trueWidth / 2 - 60, trueHeight / 2 + 10))
    else:
        if inCity:
            surface.blit(cityWallpaper, (-cam.x / parallaxFactor, -cam.y / parallaxFactor))
            surface.blit(background.cityBackground, (-cam.x, -cam.y))
        else:
            surface.blit(ruinsWallpaper, (-cam.x / parallaxFactor, -cam.y / parallaxFactor))
            surface.blit(background.ruinsBackground, (-cam.x, -cam.y))

        for b in currentBoxes:
            #b.draw(surface, cam)
            pass

        if bufferBox is not None:
            bufferBox.draw(surface, cam)

        font = pygame.font.SysFont(None, 20)
        img = font.render(str(int(ticks / fps * 100) / 100), False, "Yellow")
        surface.blit(img, (5, 5))

        player.draw(surface, cam, currentBoxes, soundHandler)

    # don't edit this code below
    upscaled = pygame.transform.scale_by(surface, upscale)
    screen.blit(upscaled, (0, 0))


def testBorder():
    if player.getHitbox().x < 0:
        player.x = -2
        player.vx = 0
    if player.getHitbox().y > levelBorder.y:
        reset(True)
    if player.getHitbox().x > levelBorder.x:
        nextLevel()


def reset(playsound=False):
    global inCity
    global currentBoxes
    global resetLock

    resetLock = True

    LevelAssets.loadLevel(currentLevel, boxesCity, boxesRuins, levelBorder, background, player)
    if playsound:
        soundHandler.playSound("death")

    #cam.focus(trueWidth, trueHeight, levelBorder)

    inCity = True
    currentBoxes = boxesCity
    player.isDead = False

def fullReset():
    global currentLevel
    global ticks
    global ticking

    currentLevel = 1
    ticking = False
    ticks = 0
    reset()


def nextLevel():
    global currentLevel
    global ticking
    global winScreen

    currentLevel += 1
    if currentLevel <= levelCount:
        reset(False)
    else:
        ticking = False
        winScreen = True


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


def quitGame():
    pygame.quit()
    exit()


def saveLevel():
    citySurface = pygame.Surface((levelBorder.x, levelBorder.y))
    cam.x = 0
    cam.y = 0
    for b in boxesCity:
        b.draw(citySurface, cam)
    pygame.image.save(citySurface, "exports/CityLayout.png")

    ruinsSurface = pygame.Surface((levelBorder.x, levelBorder.y))
    cam.x = 0
    cam.y = 0
    for b in boxesRuins:
        b.draw(ruinsSurface, cam)
    pygame.image.save(ruinsSurface, "exports/RuinsLayout.png")

init()

while True:
    main()
