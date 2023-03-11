import pygame

import box
import eventHandler
import KeyManager
import camera

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


def init():
    global screen
    global clock
    global keyManager
    global surface
    global cam

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    surface = pygame.Surface((trueWidth, trueHeight))
    pygame.display.set_caption("GameJam")
    clock = pygame.time.Clock()
    keyManager = KeyManager.KeyManager()
    cam = camera.Camera()


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
    cam.update()
    if keyManager.key_left:
        box1.x -= 1
    if keyManager.key_right:
        box1.x += 1
    if keyManager.key_jump:
        box1.y -= 1
    if keyManager.key_switch:
        box1.y += 1

    print(box2.is_colliding(box1))
def draw():
    surface.fill("Black")
    # draw below here!

    box1.draw(surface, cam)
    box2.draw(surface, cam)

    # dont edit this code below
    upscaled = pygame.transform.scale_by(surface, upscale)
    screen.blit(upscaled, (0, 0))

init()

box1 = box.Box(10, 10, 5, 4)
box2 = box.Box(50, 50, 20, 30)

while True:
    main()
