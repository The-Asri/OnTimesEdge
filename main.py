import pygame
from sys import exit
import eventHandler
import KeyManager


screen = None
surface = None
clock = None
keyManager = None
trueWidth = 150
trueHeight = 100
upscale = 8
width = trueWidth * upscale
height = trueHeight * upscale


def init():
    global screen
    global clock
    global keyManager
    global surface

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    surface = pygame.Surface((trueWidth, trueHeight))
    pygame.display.set_caption("GameJam")
    clock = pygame.time.Clock()
    keyManager = KeyManager.KeyManager()


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
    pass


def draw():
    surface.blit(testImage, (20, 20))
    upscaled = pygame.transform.scale_by(surface, upscale)
    screen.blit(upscaled, (0, 0))

init()
testImage = pygame.image.load("./graphics/schneebimer.png")
while True:
    main()
