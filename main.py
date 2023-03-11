import pygame

import box
import eventHandler
import KeyManager
import camera
import border

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

box1 = box.Box(10, 10, 5, 4)
box2 = box.Box(50, 50, 20, 30)
box3 = box.Box(100, 50, 20, 60)
box4 = box.Box(40, 80, 50, 20)


def init():
    global screen
    global clock
    global keyManager
    global surface
    global cam
    global levelBorder

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    surface = pygame.Surface((trueWidth, trueHeight))
    pygame.display.set_caption("GameJam")
    clock = pygame.time.Clock()
    keyManager = KeyManager.KeyManager()
    levelBorder = border.Border(200, 150)
    cam = camera.Camera(trueWidth, trueHeight, levelBorder, box1)


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
    cam.update(trueWidth, trueHeight, levelBorder)

    if keyManager.key_left:
        box1.x -= 1
    if keyManager.key_right:
        box1.x += 1
    if keyManager.key_up:
        box1.y -= 1
    if keyManager.key_down:
        box1.y += 1
def draw():
    surface.fill("Black")
    # draw below here!

    box1.draw(surface, cam)
    box2.draw(surface, cam)
    box3.draw(surface, cam)
    box4.draw(surface, cam)

    # dont edit this code below
    upscaled = pygame.transform.scale_by(surface, upscale)
    screen.blit(upscaled, (0, 0))

init()

cam.target = box1

while True:
    main()
