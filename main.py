import pygame
import eventHandler

screen = None
clock = None


def init():
    global screen
    global clock
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("GameJam")
    clock = pygame.time.Clock()
    print("hi")


def main():
    eventHandler.eventHandler()
    #
    #
    pygame.display.update()
    clock.tick(30)


init()

while True:
    main()
