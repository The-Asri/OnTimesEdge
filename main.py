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
boxes = []

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
    LevelAssets.loadLevel(1, boxes, levelBorder, player)
    cam = camera.Camera(trueWidth, trueHeight, levelBorder, player)


def main():
    eventHandler.eventHandler(keyManager)
    update()
    draw()
    pygame.display.update()
    clock.tick(30)
    if keyManager.key_escape:
        pygame.quit()
        exit()


def update():
    player.update(boxes, keyManager)
    cam.update(trueWidth, trueHeight, levelBorder)

def draw():
    surface.fill("Black")
    # draw below here!

    for b in boxes:
        b.draw(surface, cam)

    player.draw(surface, cam)

    # dont edit this code below
    upscaled = pygame.transform.scale_by(surface, upscale)
    screen.blit(upscaled, (0, 0))

init()

while True:
    main()
