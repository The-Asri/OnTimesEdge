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
trueWidth = 180
trueHeight = 120
upscale = 5
width = trueWidth * upscale
height = trueHeight * upscale
cityBackground = None
ruinsBackground = None
cityWallpaper = None
ruinsWallpaper = None
paralaxFactor = 8
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
currentLevel = 4
levelCount = 4
fps = 30

renderLevel = False


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
    cityBackground = ImageAssets.loadImage(7)
    ruinsBackground = ImageAssets.loadImage(8)
    LevelAssets.loadLevel(currentLevel, boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)
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

    if keyManager.key_escape:
        quitGame()
    if keyManager.key_reset and not resetLock:
        reset()
    if keyManager.key_switch and not switchLock:
        switch()

    if not keyManager.key_reset:
        resetLock = False
    if not keyManager.key_switch:
        switchLock = False

    player.update(currentBoxes, keyManager)
    if player.isDead:
        reset()
    cam.update(trueWidth, trueHeight, levelBorder)

    if bufferTime > 0:
        bufferTime -= 1
        if bufferTime <= 0:
            bufferBox = None

    testBorder()


def draw():
    surface.fill("Black")
    # draw below here!

    if inCity:
        surface.blit(cityWallpaper, (-cam.x / paralaxFactor, -cam.y / paralaxFactor))
        # surface.blit(cityBackground, (-cam.x, -cam.y))
    else:
        surface.blit(ruinsWallpaper, (-cam.x / paralaxFactor, -cam.y / paralaxFactor))
        # surface.blit(ruinsBackground, (-cam.x, -cam.y))

    for b in currentBoxes:
        b.draw(surface, cam)

    if bufferBox is not None:
        bufferBox.draw(surface, cam)

    player.draw(surface, cam)

    # don't edit this code below
    upscaled = pygame.transform.scale_by(surface, upscale)
    screen.blit(upscaled, (0, 0))


def testBorder():
    if player.getHitbox().x < 0:
        player.x = -2
        player.vx = 0
    if player.getHitbox().y > levelBorder.y:
        reset()
    if player.getHitbox().x > levelBorder.x:
        nextLevel()


def reset():
    global inCity
    global currentBoxes
    global resetLock

    resetLock = True

    LevelAssets.loadLevel(currentLevel, boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)
    inCity = True
    currentBoxes = boxesCity
    player.isDead = False


def nextLevel():
    global currentLevel

    currentLevel += 1
    if currentLevel <= levelCount:
        reset()
    else:
        print("Won!")
        quitGame()


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
